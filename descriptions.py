from flask import  Flask, request, jsonify, g

import sqlite3


app = Flask(__name__)
app.config["DEBUG"] = True



#  To get user Description
@app.route('/api/v1/resources/descriptions',methods=['GET'])
def GetDescription():
        if request.method == 'GET':
            query_parameters = request.args
            username = query_parameters.get('username')
            track_url = query_parameters.get('track_url')
            if username and track_url:
                #Todo
                #call the db and check user's is present and get the description


                return jsonify(username+"description coming soon")


#TO create new description
@app.route('/api/v1/resources/descriptions',methods=['POST'])
def InserUser():
        if request.method == 'POST':
            #get json data verify username is present and track is present. then insert it to db
            return jsonify("test post description")

app.run()
