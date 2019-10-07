
from flask import  Flask, request, jsonify, g
from werkzeug.security import generate_password_hash,check_password_hash
import sqlite3


app = Flask(__name__)
app.config["DEBUG"] = True



#  To get user profile details &
# To match user name and hashed password
@app.route('/api/v1/resources/user',methods=['GET'])
def GetUser():
        if request.method == 'GET':
            query_parameters = request.args
            username = query_parameters.get('username')
            password = query_parameters.get('hashed_password')
            if username and password:
                #Todo
                #call the db and check user is present and get the hashed password and match it


                hashed_password = generate_password_hash(password)
                authenticated = check_password_hash(hashed_password,password)
                data = hashed_password + ' ' + password + ' '+ str(authenticated)
                return jsonify(data)
            elif username:
                #Todo
                #call the db and check user is present and get the hashed password and match it

                return jsonify(username)


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
"""@app.route('/api/v1/resources/user',methods=['DELETE'])
def UpdateUserPwd():
        if request.method == 'PATCH':
            return jsonify("test patch")"""

app.run()
