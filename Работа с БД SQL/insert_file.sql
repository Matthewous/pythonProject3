insert into albums(name, release_date) values
	('Электрические жирафы', '1986.01.01'),
	('The Now Now', '2018.07.28'),
	('Горизонт событий', '2017.09.29'),
	('Иномарки', '2004.03.02'),
	('Lost on You', '2016.12.09'),
	('L Autre...', '2020.01.08'),
	('Under Pressure', '1981.10.26'),
	('A Kind of Magic', '1986.06.02'),
	('A Night at Opera', '1975.11.21'),
	('The Works', '1984.02.27'),
	('Abbey Road', '1969.09.26'),
	('My Way', '1969.03.01'),
	('Gorillaz', '2001.03.26'),
	('Demon Days', '2005.05.11');


insert into performers (name) values
	('Багровый фантомас'),
	('Gorillaz'),
	('Би-2'),
	('LP'),
	('Милен Фармер'),
	('Queen'),
	('The Beatles'),
	('Фрэнк Синатра');

insert into albums_performers (album_id, performer_id) values
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 3),
	(5, 4),
	(6, 5),
	(7, 6),
	(8, 6),
	(9, 6),
	(10, 7),
	(11, 7),
	(12, 8),
	(13, 2),
	(14, 2);
	
	
insert into genres (name) values
	('Метал'),
	('Рок'),
	('Поп'),
	('Джаз'),
	('Альтернативная'),
	('Электронная');

	
insert into genres_performers (performer_id, genre_id) values
	(1, 1),
	(2, 5),
	(3, 2),
	(3, 3),
	(4, 2),
	(5, 6),
	(6, 2),
	(7, 2),
	(8, 4);
	
insert into tracks(name, len, album_id) values
	('История, написанная сердцем',278, 1),
	('Lake Zurich', 252, 2),
	('Magic City', 239, 2),
	('Философский камень', 286, 3),
	('Виски', 197, 3),
	('Лайки', 211, 3),
	('Скользкие улицы', 339, 4),
	('Революция', 216, 4),
	('Lost on You', 266, 5),
	('Other People', 244, 5),
	('Regrets', 313, 6),
	('N oublie pas', 224, 6),
	('Under Pressure', 256, 7),
	('A kind of Magic', 261, 8),
	('Bohemian Rhapsody', 353, 9),
	('Radio GaGa', 343, 10),
	('Here comes the sun', 185, 11),
	('Come together', 258, 11),
	('My Way', 276, 12),
	('Clint Eastwood', 342, 13),
	('Feel Good', 221, 14);
	
	
insert into mixtapes (name, release_date) values
	('Queen - The Greatest Hits', '1981.10.26'),
	('The Beatles - 20 Greatest Hits', '1982.10.11'),
	('Queen - The Platinum Collection', '2000.11.13'),
	('Gorillaz - The Singles Collection 2001–2011', '2011.11.28'),
	('Mylene Farmer - Les Mots', '2001.11.26'),
	('Mylene Farmer - Histoires de', '2020.12.04'),
	('Gorillaz - D-Sides', '2007.11.19'),
	('Би-2 - Раритентный', '2006.01.01');

	
insert into tracks_mixtapes (track_id, mixtape_id) values
	(18, 2),
	(13, 1),
	(14, 1),
	(15, 1),
	(16, 1),
	(17, 1),
	(17, 2),
	(20, 4),
	(11, 5),
	(11, 6),
	(14, 3),
	(15, 3),
	(16, 3),
	(17, 3),
	(21, 7),
	(7, 8);