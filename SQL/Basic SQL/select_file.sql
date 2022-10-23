-- Домашнее задание к лекции «Select-запросы, выборки из одной таблицы»


-- название и год выхода альбомов, вышедших в 2018 году;
select name, release_date from albums where 
    release_date >= '01.01.2018' 
    and release_date < '01.01.2019'
;

-- название и продолжительность самого длительного трека
select name, len from tracks where len = (select max(len) from tracks);

-- название треков, продолжительность которых не менее 3,5 минуты
select name from tracks where len >= 210;

-- названия сборников, вышедших в период с 2018 по 2020 год включительно
select name from mixtapes where 
    release_date >= '01.01.2018' 
    and release_date < '01.01.2021'
;

-- исполнители, чье имя состоит из 1 слова
select name from performers where (LENGTH(name) - LENGTH(replace(name, ' ', ''))) = 0

-- название треков, которые содержат слово "мой"/"my"
select name from tracks where 
	name like '%My%'
	or name like '%my%'
	or name like '%Мой%'
	or name like '%мой%'
;


-- Домашнее задание к лекции «Продвинутая выборка данных» 


-- количество исполнителей в каждом жанре
select g."name" , count(*) from genres_performers gp 
	left join genres g on gp.genre_id = g.id 
	group by g."name" 
;
	
-- количество треков, вошедших в альбомы 2019-2020 годов
select count(t.id) from tracks t 
left join albums a on t.album_id = a.id 
	where a.release_date >= '01.01.2019' 
	and a.release_date < '01.01.2021'
;

-- средняя продолжительность треков по каждому альбому
select a."name", avg(len) from tracks t
	left join albums a on t.album_id = a.id 
	group by a."name"  
;

-- все исполнители, которые не выпустили альбомы в 2020 году
select p."name" from performers p 
except
	(select distinct p."name" from performers p
			left join albums_performers ap on p.id = ap.performer_id 
			left join albums a on a.id = ap.album_id
				where a.release_date between '2019-12-31' and '2021-01-01'
				order by p."name")
;

-- названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
select distinct m."name" from mixtapes m 
	left join tracks_mixtapes tm on m.id  = tm.mixtape_id
	left join tracks t on tm.track_id = t.id 
	left join albums a on t.album_id = a.id
	left join albums_performers ap on a.id = ap.album_id 
	left join performers p on ap.performer_id =p.id 
		where p."name" = 'Queen'
		
-- название альбомов, в которых присутствуют исполнители более 1 жанра
select a."name" from albums a 
	left join albums_performers ap on a.id = ap.album_id 
	left join performers p on ap.performer_id = p.id 
	left join genres_performers gp on p.id = gp.performer_id 
	left join genres g on gp.genre_id = g.id 
	group by a."name" 
	having count(distinct g."name") > 1
;

-- наименование треков, которые не входят в сборники
select t."name" from tracks t 
	left join tracks_mixtapes tm on t.id = tm.track_id 
	left join mixtapes m on tm.mixtape_id = m.id 
		where m."name" is null
;

-- исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
select p."name" from tracks t 
	left join albums a on t.album_id = a.id 
	left join albums_performers ap on a.id = ap.album_id
	left join performers p on ap.performer_id = p.id 
	group by p."name", t.len 
		having t.len = (select min(t.len) from tracks t)
;		

-- название альбомов, содержащих наименьшее количество треков
select distinct a."name" 
	from albums as a
	left join tracks t on t.album_id = a.id
	where t.album_id in (
    	select album_id
    	from tracks
    	group by album_id
    	having count(id) = (
        	select count(id)
        	from tracks
        	group by album_id
        	order by count
        	limit 1
    	)
	)
	order by a.name
;
		