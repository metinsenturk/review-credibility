
-------------------------------------------------------BOOKS-------------------------------------------------------------------------
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
-------------------------------------------------BUSINESS------------------------------------------------------------------------------
DROP TABLE IF EXISTS Business
CREATE TABLE Business (
 business_id nvarchar(100) NULL, 
 name nvarchar(100) NULL, 
 address nvarchar(100) NULL,
 city nvarchar(100) NULL,
 state nvarchar(20) NULL,
 postal_code int NULL,
 latitude float NULL,
 longitude float NULL,
 stars float NULL,
 review_count int NULL,
 is_open int NULL,
 RestaurantsTakeOut nvarchar(20) NULL,
 BusinessParking_garage nvarchar(20) NULL,
 BusinessParking_street nvarchar(20) NULL,
 BusinessParking_validated nvarchar(20) NULL,
 BusinessParking_lot nvarchar(20) NULL,
 BusinessParking_valet nvarchar(20) NULL,
 categories nvarchar(max) NULL,
 hours nvarchar(max) NULL,
 ) 

INSERT INTO Business
SELECT * FROM

OPENROWSET(
	BULK 'business.json', 
	DATA_SOURCE = 'YelpJsonFiles',
	SINGLE_CLOB
) AS json
CROSS APPLY OPENJSON(BulkColumn)
 WITH(	business_id nvarchar(100), 
		name nvarchar(100), 
		address nvarchar(100),
		city nvarchar(100) ,
		state nvarchar(20),
		postal_code int '$.[postal code]',
		latitude float ,
		longitude float ,
		stars float ,
		review_count int ,
		is_open int,
		RestaurantsTakeOut nvarchar(20) '$.attributes.RestaurantsTakeOut' ,
		BusinessParking_garage nvarchar(20) '$.attributes.BusinessParking.garage',
		BusinessParking_street nvarchar(20) '$.attributes.BusinessParking.street',
		BusinessParking_validated nvarchar(20) '$.attributes.BusinessParking.validated',
		BusinessParking_lot nvarchar(20) '$.attributes.BusinessParking.lot',
		BusinessParking_valet nvarchar(20) '$.attributes.BusinessParking.valet',
		categories nvarchar(max) as json,
		hours nvarchar(max) as json,
 ) as business
	  
 --outer apply openjson(categories) with ( cat_ nvarchar(100) '$')
 --outer apply openjson(hours) with ( hours_ nvarchar(100) '$')

;

----------------------------------------------------------REVIEW ------------------------------------------------------

DROP TABLE IF EXISTS Review
CREATE TABLE Review (
		review_id nvarchar(100) ,
		user_id nvarchar(100),
		business_id nvarchar(100),
		stars float,
		date date,
		text nvarchar(max),
		useful int,
		funny int,
		cool int
		)
insert into Review
SELECT * FROM

OPENROWSET(
	BULK 'review.json', 
	DATA_SOURCE = 'YelpJsonFiles',
	SINGLE_CLOB
) AS json
CROSS APPLY OPENJSON(BulkColumn)
 WITH( review_id nvarchar(100) ,
		user_id nvarchar(100),
		business_id nvarchar(100),
		stars float,
		date date,
		text nvarchar(max),
		useful int,
		funny int,
		cool int ) as review
;

--------------------------------------------------CHECKING----------------------------------------------------------------------------
DROP TABLE IF EXISTS Checking
CREATE TABLE Checking (
	business_id nvarchar(100),
	date nvarchar(100)  -- list of date in csv format
	)
insert into Checking
SELECT * FROM

OPENROWSET(
	BULK 'checking.json', 
	DATA_SOURCE = 'YelpJsonFiles',
	SINGLE_CLOB
) AS json
CROSS APPLY OPENJSON(BulkColumn)
 WITH(	business_id nvarchar(100),
		date nvarchar(100)

		) as checking
;
---------------------------------------------------------TIP------------------------------------------------------------
DROP TABLE IF EXISTS Tip
CREATE TABLE Tip (
	text nvarchar(100),
	date date,  -- list of date in csv format
	compliment_count int,
	business_id nvarchar(100),
	user_id nvarchar(100)
	)
insert into Tip
SELECT tip.* FROM

OPENROWSET(
	BULK 'tip.json', 
	DATA_SOURCE = 'YelpJsonFiles',
	SINGLE_CLOB
) AS json
CROSS APPLY OPENJSON(BulkColumn)
 WITH(	text nvarchar(100),
		date date,  -- list of date in csv format
		compliment_count int,
		business_id nvarchar(100),
		user_id nvarchar(100) 
		) as tip
----------------------------------------------------PHOTO----------------------------------------------------------------------

DROP TABLE IF EXISTS Photo
CREATE TABLE Photo (
		photo_id nvarchar(100),
		business_id nvarchar(100),
		caption nvarchar(100),
		label nvarchar(100)
		)

insert into Photo
SELECT * FROM

OPENROWSET(
	BULK 'photo.json', 
	DATA_SOURCE = 'YelpJsonFiles',
	SINGLE_CLOB
) AS json
CROSS APPLY OPENJSON(BulkColumn)
 WITH(	photo_id nvarchar(100),
		business_id nvarchar(100),
		caption nvarchar(100),
		label nvarchar(100)

		) as photo