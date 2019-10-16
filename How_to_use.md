To run the app:  

FLASK_APP=user flask init
FLASK_APP=user flask run


USER Microservice:


To retrieve user's profile:

GET:  curl -v  'http://127.0.0.1:5000/api/v1/resources/user?username=user_pavan'


To match username and password:

GET:   curl -v  'http://127.0.0.1:5000/api/v1/resources/user?username=user_pavan&password=12ds'



To create a new user profile:

POST:  curl -X POST -v  http://127.0.0.1:5000/api/v1/resources/user -d  '{"username": "joker12", "display_name": "Joker", "password": "serious",  "homepage_url": "joker.com", "email": "joker@joker.com"}'

Change Users Password:

PATCH:  curl -X PATCH curl -v http://127.0.0.1:5000/api/v1/resources/user?username=joker12 -d '{ "password": "serious123" }'

To delete user:

DELETE: curl -X DELETE -v  'http://127.0.0.1:5000/api/v1/resources/user?username=user_pavan'






Description Microservice:


GET:  curl  http://127.0.0.1:5000/api/v1/resources/descriptions?username=user_pavan2&track_url=/tracks?url=%22Yeah.mp3%22


POST:  curl -X POST curl  http://127.0.0.1:5000/api/v1/resources/descriptions -d '{"username":"test1", "track_url":"vale","description":"dddasd"}'
query ="INSERT INTO description(username, track_url, description) VALUES('test','test','domething');"
