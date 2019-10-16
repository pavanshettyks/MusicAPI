
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
        db = g._database = sqlite3.connect('MUSICDATABASE')
        db.row_factory = make_dicts
    db.cursor().execute("PRAGMA foreign_keys=ON")
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
        with app.open_resource('music_store.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()



##################################

def authenticate_user(username,password):
    query = "SELECT hashed_password FROM user WHERE username=?;"
    to_filter= []
    to_filter.append(username)
    results = query_db(query, to_filter)
    if not results:
        return jsonify(message="User Authentication unsuccessful. Try with new password"),401

    authenticated = check_password_hash(results[0]['hashed_password'],password)
    if authenticated:
        return jsonify(message="User Authentication successful"),200

    return jsonify(message="User Authentication unsuccessful. Try with new password"),401


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
                #call the db and check user is present and get the hashed password and match it
                return authenticate_user(username,password)

            elif username:
                #call the db and check user . If yes retrieve the data
                query = "SELECT username,display_name,email,homepage_url FROM user WHERE username=?;"
                to_filter.append(username)
                results = query_db(query, to_filter)
                if not results:
                    return jsonify(message="No user present. Please provide valid username"),404
                else:
                    resp = jsonify(results)
                    resp.headers['Location'] = 'http://127.0.0.1:5000/api/v1/resources/user?username='+username
                    resp.status_code = 200
                    #resp.headers['mimetype']='application/json'
                    return resp




#TO create new user
@app.route('/api/v1/resources/user',methods=['POST'])
def InserUser():
        if request.method == 'POST':
            data = request.get_json(force= True)
            #print(type(data))
            required_fields = ['username', 'display_name', 'password', 'homepage_url', 'email']
            username = data['username']
            password = data['password']

            #To check username and password matching
            if not all([field in data for field in required_fields]):
                return authenticate_user(username,password)

            display_name  = data['display_name']
            email  = data['email']
            homepage_url  = data['homepage_url']
            hashed_password = generate_password_hash(password)
            executionState:bool = False
            query ="INSERT INTO user(username, display_name, hashed_password, homepage_url, email) VALUES('"+username+"','"+display_name+"','"+hashed_password+"','"+homepage_url+"','"+email+"');"
            #print(query)
            cur = get_db().cursor()
            try:
                cur.execute(query)
                if(cur.rowcount >=1):
                    executionState = True
                get_db().commit()
            except:
                get_db().rollback()
                #print("Error")
            finally:
                if executionState:
                    resp = jsonify(message="Data Instersted Sucessfully")
                    resp.headers['Location'] = 'http://127.0.0.1:5000/api/v1/resources/user?username='+username
                    resp.status_code = 201
                    return resp
                else:
                    return jsonify(message="Failed to insert data."), 409


#To update user password
@app.route('/api/v1/resources/user',methods=['PATCH'])
def UpdateUserPwd():
        if request.method == 'PATCH':
            to_filter = []
            query_parameters = request.args
            username = query_parameters.get('username')
            data = request.get_json(force= True)
            #print(type(data))
            password = data['password']
            hashed_password = generate_password_hash(password)
            query = "SELECT * FROM user WHERE username=?;"
            to_filter.append(username)
            results = query_db(query, to_filter)
            if not results:
                return jsonify(message="No user present. Please provide valid username"),404
            else:
                executionState:bool = False
                cur = get_db().cursor()
                try:
                    cur.execute("UPDATE user SET hashed_password=? WHERE username=?",(hashed_password,username,))
                    if cur.rowcount >= 1:
                        executionState = True
                    get_db().commit()

                except:
                        get_db().rollback()
                        #print("Error")
                finally:
                        if executionState:
                            resp = jsonify(message="Password updated successfully")
                            resp.headers['Location'] = 'http://127.0.0.1:5000/api/v1/resources/user?username='+username
                            resp.status_code = 200
                            return resp

                        else:
                            return jsonify(message="Failed to update password"), 409




#To delete user
@app.route('/api/v1/resources/user',methods=['DELETE'])
def DeleteUser():
        if request.method == 'DELETE':
            query_parameters = request.args
            username = query_parameters.get('username')
            executionState:bool = False
            cur = get_db().cursor()
            try:
                cur.execute("DELETE FROM user WHERE username=?",(username,))
                if cur.rowcount >= 1:
                    executionState = True
                get_db().commit()

            except:
                    get_db().rollback()
                    #print("Error")
            finally:
                    if executionState:
                        return jsonify(message="Data deleted sucessFully "), 200
                    else:
                        #possibly no user data . so 404
                        return jsonify(message="Failed to delete data"), 404

app.run()
