To run microservice "TRACKS":
FLASK_APP=tracks flask init
FLASK_APP=tracks flask run


To get/retrieve all track's:
GET: curl -v 'http://127.0.0.1:5200/api/v1/resources/tracks'


To get a particular track
GET: curl -v 'http://127.0.0.1:5200/api/v1/resources/tracks?track_url=mp3'


To create a new track
POST: curl -X POST -v http://127.0.0.1:5200/api/v1/resources/tracks -d '{"track_title": "tango", "album_title": "Joker", "artist": "brad", "length": "12:12:12", "track_url": "alpha", "album_art_url": "tuffy"}'


To edit a track
PUT: curl -X PUT -v http://127.0.0.1:5200/api/v1/resources/tracks?track_url=tp3 -d '{"track_title": "joker12", "album_title": "Joker", "artist": "rf", "length": "12:12:12", "track_url": "tp3", "album_art_url": "wser"}'

To delete a track
DELETE: curl -X DELETE -v 'http://127.0.0.1:5200/api/v1/resources/tracks?track_url=tp3'




To run microservice "PLAYLIST":
FLASK_APP=playlist flask init
FLASK_APP=playlist flask run


To Create a new playlist
POST: curl -X POST -v http://127.0.0.1:5300/api/v1/resources/playlist -d '{ "all_tracks": [
            {
                "track_url": "tp3"
            },
            {
                "track_url": "bp3"
            },
            {
                "track_url": "mp3"
            }
        ],"playlist_title": "AllIsWell", "username": "user_priyanka", "description": "One2Three"}'


To retrieve a playlist:
GET: curl -v 'http://127.0.0.1:5300/api/v1/resources/playlist?playlist_title=AllIsWell&username=user_priyanka'



To delete a playlist:
DELETE: curl -X DELETE -v 'http://127.0.0.1:5300/api/v1/resources/playlist?username=user_priyanka&playlist_title=All'

To list all playlists:
GET: curl -v 'http://127.0.0.1:5300/api/v1/resources/playlist'


To list playlists created by a particular user
GET: curl -v 'http://127.0.0.1:5300/api/v1/resources/playlist?username=user_pavan'
