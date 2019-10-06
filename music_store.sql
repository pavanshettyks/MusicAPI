-- $ sqlite3 music_store.db < sqlite.sql

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS description;

CREATE TABLE user (
	username VARCHAR primary key,
	hashed_password VARCHAR,
	display_name VARCHAR,
	homepage_url VARCHAR,
	email VARCHAR
);

CREATE TABLE description (
	username VARCHAR primary key,
	track_url VARCHAR,
	description VARCHAR
);

CREATE TABLE tracks (
	track_title VARCHAR,
	album_title VARCHAR,
	artist VARCHAR,
	length TIME,
	track_url VARCHAR primary key,
	album_art_url VARCHAR
);

CREATE TABLE playlist (
	playlist_title VARCHAR primary key,
	username VARCHAR primary key,
	description VARCHAR
);

CREATE TABLE playlist_tracks (
	username VARCHAR primary key,
	title VARCHAR primary key,
	track_url VARCHAR
);