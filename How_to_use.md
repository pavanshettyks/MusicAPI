To run the app:  
FLASK_APP=user flask init
FLASK_APP=user flask run


USER Microservice

GET:  curl  http://127.0.0.1:5000/api/v1/resources/user?username=pk

GET: curl  http://127.0.0.1:5000/api/v1/resources/user?username=pk&hashed_password=12ds


POST:   curl -d "param1=value1&param2=value2" -X POST curl  http://127.0.0.1:5000/api/v1/resources/user


PATCH:  curl -d "param1=value1&param2=value2" -X PATCH curl  http://127.0.0.1:5000/api/v1/resources/user


Description Microservice:

GET:  curl  http://127.0.0.1:5000/api/v1/resources/descriptions?username=user_pavan2&track_url=/tracks?url=%22Yeah.mp3%22

POST:  curl -X POST curl  http://127.0.0.1:5000/api/v1/resources/descriptions -d '{"username":"test1", "track_url":"vale","description":"dddasd"}'
