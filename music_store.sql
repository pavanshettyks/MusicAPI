-- $ sqlite3 music_store.db < sqlite.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS description;
DROP TABLE IF EXISTS tracks;
DROP TABLE IF EXISTS playlist;
DROP TABLE IF EXISTS playlist_tracks;

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
	username VARCHAR,
	track_url VARCHAR,
	description VARCHAR,
	description_id INTEGER primary key,
	FOREIGN KEY (username) REFERENCES user (username),
	FOREIGN KEY (track_url) REFERENCES tracks (track_url)
);

INSERT INTO description(username, track_url, description) VALUES('user_pavan','/tracks?url="Stronger.mp3"', 'workout song by kanye west');
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

INSERT INTO tracks(track_title, album_title, artist, length, track_url) VALUES('Stronger','Graduation', 'Kanye West', 00:05:11,'/tracks?url="Stronger.mp3"');
INSERT INTO tracks(track_title, album_title, artist, length, track_url) VALUES('Yeah!','Confessions', 'Usher', 00:04:10,'/tracks?url="Yeah!.mp3"');
INSERT INTO tracks(track_title, album_title, artist, length, track_url) VALUES('I Gotta Feeling','The E.N.D.', 'The Black Eyed Peas', 00:04:48,'/tracks?url="I Gotta Feeling.mp3"');


CREATE TABLE playlist (
	playlist_title VARCHAR primary key,
	username VARCHAR primary key,
	description VARCHAR
);

INSERT INTO playlist(playlist_title, username, description) VALUES('All','user_priyanka', 'This playlist contains all of my songs');
INSERT INTO playlist(playlist_title, username, description) VALUES('Some','user_anthony', 'This playlist contains some of my songs');

CREATE TABLE playlist_tracks (
	username VARCHAR,
	title VARCHAR primary key,
	track_url VARCHAR,
	FOREIGN KEY (username) REFERENCES user(username)
);

INSERT INTO playlist_tracks(username, title, track_url) VALUES('user_priyanka','All', '/tracks?url="Stronger.mp3"');
INSERT INTO playlist_tracks(username, title, track_url) VALUES('user_priyanka','All', '/tracks?url="Yeah!.mp3"');
INSERT INTO playlist_tracks(username, title, track_url) VALUES('user_priyanka','All', '/tracks?url="I Gotta Feeling.mp3"');
INSERT INTO playlist_tracks(username, title, track_url) VALUES('user_anthony','Some', '/tracks?url="Stronger.mp3"');
INSERT INTO playlist_tracks(username, title, track_url) VALUES('user_anthony','Some', '/tracks?url="Yeah!.mp3"');


