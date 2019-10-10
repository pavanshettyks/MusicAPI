To run the app:  
FLASK_APP=user flask init
FLASK_APP=user flask run


USER Microservice:

GET:  curl -v  'http://127.0.0.1:5000/api/v1/resources/user?username=user_pavan'

GET:   curl -v  'http://127.0.0.1:5000/api/v1/resources/user?username=user_pavan&password=12ds'

POST:  curl -X POST -v  http://127.0.0.1:5000/api/v1/resources/user -d  '{"username": "joker12", "display_name": "Joker", "password": "serious",  "homepage_url": "joker.com", "email": "joker@ser.com"}'

DELETE: curl -X DELETE -v  'http://127.0.0.1:5000/api/v1/resources/user?username=user_pavan'


PATCH:  curl -d "param1=value1&param2=value2" -X PATCH curl  http://127.0.0.1:5000/api/v1/resources/user



Description Microservice:

GET:  curl  http://127.0.0.1:5000/api/v1/resources/descriptions?username=user_pavan2&track_url=/tracks?url=%22Yeah.mp3%22

POST:  curl -X POST curl  http://127.0.0.1:5000/api/v1/resources/descriptions -d '{"username":"test1", "track_url":"vale","description":"dddasd"}'

query ="INSERT INTO description(username, track_url, description) VALUES('test','test','domething');"
