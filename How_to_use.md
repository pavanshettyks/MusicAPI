## Instructions to use the Microservice:

To initailize th database use command:   FLASK_APP=user flask init

//FLASK_APP=user flask run

To start all the Microservices use command:   foreman start


# USER Microservice:


To a retrieve User's profile (GET method) use the following curl command:

  curl -v  'http://127.0.0.1:5000/api/v1/resources/user?username=user_pavan'


To authenticate a User use the following curl command:

GET:   curl -v  'http://127.0.0.1:5000/api/v1/resources/user?username=user_pavan&password=12ds'


To create a new User profile use the following curl command (POST method):

POST:  curl -X POST -v  http://127.0.0.1:5000/api/v1/resources/user -d  '{"username": "joker12", "display_name": "Joker", "password": "serious",  "homepage_url": "joker.com", "email": "joker@joker.com"}'


Change User's Password use the following curl command:

PATCH:  curl -X PATCH -v http://127.0.0.1:5000/api/v1/resources/user?username=joker12 -d '{ "password": "serious123" }'


To delete a User use the following curl command:

DELETE: curl -X DELETE -v  'http://127.0.0.1:5000/api/v1/resources/user?username=user_pavan'




# Description Microservice:

Retrieve a User’s Description of a track

GET:  curl  http://127.0.0.1:5000/api/v1/resources/descriptions?username=user_pavan2&track_url=/tracks?url=%22Yeah.mp3%22


To set a User’s Description of a track  use the following curl command:

POST:  curl -X POST  http://127.0.0.1:5000/api/v1/resources/descriptions -d '{"username":"user_pavan", "track_url":"vale","description":"Looks good"}'
