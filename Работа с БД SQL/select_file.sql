select name, release_date from albums where 
    release_date >= '01.01.2018' 
    and release_date < '01.01.2019'
;

select name, len from tracks where len = (select max(len) from tracks);

select name from tracks where len >= 210;

select name from mixtapes where 
    release_date >= '01.01.2018' 
    and release_date < '01.01.2021'
;

select name from performers where (LENGTH(name) - LENGTH(replace(name, ' ', ''))) = 0

select name from tracks where 
	name like '%My%'
	or name like '%my%'
	or name like '%Мой%'
	or name like '%мой%'
;