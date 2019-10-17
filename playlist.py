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
        db = g._database = sqlite3.connect('MUSICDATABASE')
        db.row_factory = make_dicts
    db.cursor().execute("PRAGMA foreign_keys=ON")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.cli.command('init')
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('music_store.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()



def query_db(query,args=(),one=False):
    cur = get_db().execute(query,args)
    rv = cur.fetchall()
    cur.close()
    return(rv[0] if rv else None) if one else rv



#TO create new playlist
def generate_multiple_insert(all_tracks,username,playlist_title):
    querry = "INSERT INTO playlist_tracks (username, playlist_title,track_url) VALUES"
    value_querry = ""
    track_url =""
    for track in all_tracks:
         val = track['track_url'].split('/api/v1/resources/tracks?track_url=')

         if len(val) == 1:
             track_url = val[0]
         else:
             track_url = val[1]
         value_querry = value_querry + "('"+username+"','"+playlist_title+"','"+track_url+"') ,"
    value_querry = value_querry[:-1]+';'
    querry = querry + value_querry
    #print(querry)
    return querry


#TO create new playlist
@app.route('/api/v1/resources/playlist',methods=['POST'])
def InsertPlaylist():
        if request.method == 'POST':
            data =request.get_json(force= True)
            to_filter = []
            playlist_title = data['playlist_title']
            username = data['username']
            description = data['description']
            all_tracks = data['all_tracks']
            executionState:bool = False
            query = "SELECT playlist_title FROM playlist WHERE playlist_title=? AND username =? ;"
            to_filter.append(playlist_title)
            to_filter.append(username)
            results = query_db(query, to_filter)
            if not results:
                query ="INSERT INTO playlist(playlist_title,username, description) VALUES('"+playlist_title+"','"+username+"','"+description+"');"
                cur = get_db().cursor()
                cur2 = get_db().cursor()
                try:
                    cur.execute(query)
                    if(cur.rowcount >=1):
                        executionState = True
                    if all_tracks:
                        multi_insert_querry = generate_multiple_insert(all_tracks,username,playlist_title)
                        #print(multi_insert_querry)
                        cur2.execute(multi_insert_querry)

                    get_db().commit()
                except:
                    get_db().rollback()
                    executionState = False
                    #print("error")
                finally:
                    if executionState:
                        resp = jsonify(message="Data Instersted Sucessfully")
                        resp.headers['Location'] = 'http://127.0.0.1:5300/api/v1/resources/playlist?playlist_title='+playlist_title+'&'+'username='+username
                        resp.status_code = 201
                        return resp
                    else:
                        return jsonify(message="Failed to insert data"), 409
            else:
                return jsonify(message="Failed to insert data."), 409


#to delete a playlist
def delete_all_tracks(playlist_title,username):
    to_filter = []
    query = "SELECT * FROM playlist_tracks WHERE username=? AND playlist_title=?;"
    to_filter.append(username)
    to_filter.append(playlist_title)
    res = query_db(query, to_filter)
    cur = get_db().cursor()
    if res:

        try:
            cur.execute("DELETE FROM playlist_tracks WHERE playlist_title=? AND username =?;",(playlist_title,username,))
            if cur.rowcount >= 1:
                executionState = True

            get_db().commit()
        except:
                get_db().rollback()

        finally:
            print("deleted relevant playlist_tracks data")



#to delete a playlist
@app.route('/api/v1/resources/playlist', methods=['DELETE'])
def DeletePlaylist():
        if request.method == 'DELETE':
            query_parameters = request.args
            playlist_title = query_parameters.get('playlist_title')
            username = query_parameters.get('username')
            executionState:bool = False
            cur = get_db().cursor()
            try:
                cur.execute("DELETE FROM playlist WHERE playlist_title=? AND username =?;",(playlist_title,username,))

                if cur.rowcount >= 1:
                    executionState = True
                get_db().commit()

            except:
                    get_db().rollback()
                    #print("Error")
            finally:
                    if executionState:
                        delete_all_tracks(playlist_title,username)
                        return jsonify(message="Data SucessFully deleted"), 200
                    else:
                        return jsonify(message="Failed to delete data"), 409



#to list  playlists
@app.route('/api/v1/resources/playlist', methods=['GET'])
def GetAllPlaylist():
    if request.method=='GET':
        query_parameters = request.args
        playlist_title = query_parameters.get('playlist_title')
        username = query_parameters.get('username')
        to_filter = []
        if username and playlist_title:
            query = "SELECT playlist_title,username,description FROM playlist WHERE username=? AND playlist_title= ?;"
            to_filter.append(username)
            to_filter.append(playlist_title)

            results = query_db(query, to_filter)
            if not results:
                return jsonify(message="No playlist present"), 404
            else:
                query = "SELECT track_url FROM playlist_tracks WHERE username=? AND playlist_title=?;"
                all_tracks = query_db(query, to_filter)
                for track in all_tracks:
                    track['track_url'] = 'http://127.0.0.1:5200/api/v1/resources/tracks?track_url='+track['track_url']
                results[0]['all_tracks']= all_tracks

                resp = jsonify(results)

                resp.headers['Location']='http://127.0.0.1:5300/api/v1/resources/playlist?username='+username+'&playlist_title='+playlist_title
                resp.status_code = 200
                return resp

        elif username:
            query = "SELECT playlist_title,username,description FROM playlist WHERE username=?;"
            to_filter.append(username)
            results = query_db(query, to_filter)
            if not results:
                return jsonify(message="No playlist present"), 404
            else:
                resp = jsonify(results)
                resp.headers['Location']='http://127.0.0.1:5300/api/v1/resources/playlist?username='+username
                resp.status_code = 200
                return resp
        else:
            query = "SELECT playlist_title,username,description FROM playlist;"

            results = query_db(query, to_filter)
            if not results:
                return jsonify(message="No playlist present"), 404
            else:
                resp = jsonify(results)
                resp.headers['Location']='http://127.0.0.1:5300/api/v1/resources/playlist'
                resp.status_code = 200
                return resp



app.run()
