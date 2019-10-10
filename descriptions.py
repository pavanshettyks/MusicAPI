from flask import  Flask, request, jsonify, g

import sqlite3


app = Flask(__name__)
app.config["DEBUG"] = True

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('TESTDATABASE')
        db.row_factory = make_dicts
    return db



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.cli.command('init')
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('test.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


#  To get user Description
@app.route('/api/v1/resources/descriptions',methods=['GET'])
def GetDescription():
        if request.method == 'GET':
            query_parameters = request.args
            username = query_parameters.get('username')
            track_url = query_parameters.get('track_url')
            to_filter = []
            if username and track_url:
                #Todo
                #call the db and check user's is present and get the description
                query = "SELECT username,track_url,description FROM description WHERE username=? AND  track_url=? ;"
                to_filter.append(username)
                to_filter.append(track_url)
                results = query_db(query, to_filter)
                if not results:
                    return jsonify(message="No description present"),404
                return jsonify(results),200


#TO create new description
@app.route('/api/v1/resources/descriptions',methods=['POST'])
def InserUser():
        if request.method == 'POST':
            data =request.get_json(force= True)
            username = data['username']
            track_url = data['track_url']
            description = data['description']
            #to_filter = []
            #print(request.json['username'])
            executionState:bool = False
            if user_name and track_url and description:
            #get json data verify username is present and track is present. then insert it to db
                query ="INSERT INTO description(username, track_url, description) VALUES('"+username+"','"+track_url+"','"+description+"');"
                print(query)
                cur = get_db().cursor()
                try:
                    cur.execute(query)
                    if(cur.rowcount >=1):
                        executionState = True
                    get_db().commit()
                except:
                    get_db().rollback()
                    print("Error")
                finally:
                    if executionState:
                        return jsonify(message="Data Instersted Sucessfully"),201
                    else:
                        return jsonify(message="Failed to insert data"), 409

app.run()
