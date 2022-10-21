-- Создание базы данных

CREATE TABLE IF NOT EXISTS Genres (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT null
);

CREATE TABLE IF NOT EXISTS Performers (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT null
);

CREATE TABLE IF NOT EXISTS Albums (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL,
	release_date DATE
);

CREATE TABLE IF NOT EXISTS Mixtapes (
	id SERIAL PRIMARY KEY,
	name VARCHAR(80) NOT NULL,
	release_date DATE
);

CREATE TABLE IF NOT EXISTS Tracks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	len numeric not null,
	album_id INTEGER not null references Albums(id) 
);

CREATE TABLE IF NOT EXISTS Genres_performers (
	genre_id integer references Genres(id),
	performer_id integer references Performers(id)
);

CREATE TABLE IF NOT EXISTS Albums_performers (
	album_id integer references Albums(id),
	performer_id integer references Performers(id)
);

CREATE TABLE IF NOT EXISTS Tracks_mixtapes (
	track_id integer references Tracks(id),
	mixtape_id integer references Mixtapes(id)
);