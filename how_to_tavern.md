(initialize database and microservices)
First up run:
pip install tavern
pip install tavern[pytest]
next run tavern script:
py.test test_user.tavern.yaml -v
py.test test_descriptions.tavern.yaml -v
py.test test_tracks.tavern.yaml -v
py.test test_playlist.tavern.yaml -v
