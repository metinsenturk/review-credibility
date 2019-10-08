-- create table
DROP TABLE IF EXISTS Books
CREATE TABLE Books (
 id nvarchar(100), name nvarchar(100), price float,
 pages_i int, author nvarchar(100)

)

--INSERT INTO Books
SELECT * FROM

OPENROWSET(
	BULK 'books.json', 
	DATA_SOURCE = 'YelpJsonFiles',
	SINGLE_CLOB
) AS json
CROSS APPLY OPENJSON(BulkColumn)
 WITH( iddfgdf nvarchar(100) '$.id', name nvarchar(100), price float,
 pages_i int, author nvarchar(100), genre_s nvarchar(100), cat nvarchar(max) as json
 ) AS book
 outer apply openjson(cat) with ( cat_ nvarchar(8) '$')
;