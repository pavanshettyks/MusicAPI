
from flask import  Flask, request, jsonify, g
import sqlite3


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/user',methods=['GET'])
def GetUser():
        if request.method == 'GET':
            return jsonify("test")


@app.route('/user',methods=['POST'])
def InserUser():
        if request.method == 'POST':
            return jsonify("test post")


app.run()
