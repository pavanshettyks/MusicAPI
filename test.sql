-- $ sqlite3 music_store.db < sqlite.sql

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS tracks;
DROP TABLE IF EXISTS description;

CREATE TABLE user (
	username VARCHAR primary key,
	hashed_password VARCHAR,
	display_name VARCHAR,
	homepage_url VARCHAR,
	email VARCHAR
);

INSERT INTO user(username, display_name, homepage_url, email) VALUES('user_anthony','Anthony', '/user?username=user_anthony', 'anthony@csu.fullerton.edu');
INSERT INTO user(username, display_name, homepage_url, email) VALUES('user_pavan','Pavan', '/user?username=user_pavan','pavan@csu.fullerton.edu');
INSERT INTO user(username, display_name, homepage_url, email) VALUES('user_priyanka','Priyanka', '/user?username=user_priyanka','priyanka@csu.fullerton.edu');


CREATE TABLE description (
	username VARCHAR primary key,
	track_url VARCHAR,
	description VARCHAR
);

INSERT INTO description(username, track_url, description) VALUES('user_priyanka','/tracks?url="Stronger.mp3"', 'workout song by kanye west');
INSERT INTO description(username, track_url, description) VALUES('user_pavan','/tracks?url="Yeah!.mp3"', 'favorite usher song');
INSERT INTO description(username, track_url, description) VALUES('user_anthony','/tracks?url="I Gotta Feeling.mp3"', 'classic black eyed peas song');

CREATE TABLE tracks (
	track_title VARCHAR,
	album_title VARCHAR,
	artist VARCHAR,
	length TIME,
	track_url VARCHAR primary key,
	album_art_url VARCHAR
);

INSERT INTO tracks(track_title, album_title, artist, length, track_url, album_art_url) VALUES('Stronger','Graduation', 'Kanye West', '00:05:11','/tracks?url="Stronger.mp3"', 'alpha');
INSERT INTO tracks(track_title, album_title, artist, length, track_url, album_art_url) VALUES('Yeah!','Confessions', 'Usher', '00:04:10','/tracks?url="Yeah.mp3"', 'beta');
INSERT INTO tracks(track_title, album_title, artist, length, track_url, album_art_url) VALUES('I Gotta Feeling','The E.N.D.', 'The Black Eyed Peas', '00:04:48','/tracks?url="ng.mp3"', 'delta');
