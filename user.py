
from flask import  Flask, request, jsonify, g
from werkzeug.security import generate_password_hash,check_password_hash
import sqlite3


app = Flask(__name__)
app.config["DEBUG"] = True


#################code will be moved
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



##################################
#  To get user profile details &
# To match user name and hashed password
@app.route('/api/v1/resources/user',methods=['GET'])
def GetUser():
        if request.method == 'GET':
            query_parameters = request.args
            username = query_parameters.get('username')
            password = query_parameters.get('password')
            to_filter= []
            if username and password:
                #Todo
                #call the db and check user is present and get the hashed password and match it
                #hashed_password = generate_password_hash(password)
                query = "SELECT hashed_password FROM user WHERE username=?;"
                to_filter.append(username)
                results = query_db(query, to_filter)
                if not results:
                    return jsonify("No user present"),404
                #return jsonify(results[hashed_password]),200
                authenticated = check_password_hash(results[0]['hashed_password'],password)
                if authenticated:
                    return jsonify("User Authentication successful. Username and stored password match"),200

                return jsonify("User Authentication unsuccessful. Username and stored password doent match. Try with new password"),200

            elif username:
                #Todo
                #call the db and check user is present and get the hashed password and match it
                query = "SELECT username,display_name,email,homepage_url FROM user WHERE username=?;"
                to_filter.append(username)
                results = query_db(query, to_filter)
                if not results:
                    return jsonify("No user present"),404
                return jsonify(results),200



#TO create new user
@app.route('/api/v1/resources/user',methods=['POST'])
def InserUser():
        if request.method == 'POST':
            return jsonify("test post")

#To update user password
@app.route('/api/v1/resources/user',methods=['PATCH'])
def UpdateUserPwd():
        if request.method == 'PATCH':
            return jsonify("test patch")

#To delete user
@app.route('/api/v1/resources/user',methods=['DELETE'])
def DeleteUser():
        if request.method == 'DELETE':
            return jsonify("test delete")

app.run()
