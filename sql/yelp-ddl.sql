
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
DROP TABLE IF EXISTS Businesses
CREATE TABLE Businesses (
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
	monday nvarchar(200) NULL,
	tuesday nvarchar(200) NULL,
	wednesday nvarchar(200) NULL,
	thursday nvarchar(200)  NULL,
	friday nvarchar(200) NULL,
	saturday nvarchar(200) NULL,
	sunday nvarchar(200) NULL,
) 

INSERT INTO Businesses
SELECT business.* FROM

OPENROWSET(
	BULK 'business_x.json', 
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
		monday nvarchar(200) '$.hours.Monday',
		tuesday nvarchar(200) '$.hours.Tuesday',
		wednesday nvarchar(200) '$.hours.Wednesday',
		thursday nvarchar(200) '$.hours.Thursday',
		friday nvarchar(200) '$.hours.Friday',
		saturday nvarchar(200) '$.hours.Saturday',
		sunday nvarchar(200) '$.hours.Sunday'
 ) as business
	  
 --outer apply openjson(categories) with ( cat_ nvarchar(100) '$')
 --outer apply openjson(hours) with ( hours_ nvarchar(100) '$')

;

----------------------------------------------------------REVIEW ------------------------------------------------------

DROP TABLE IF EXISTS Reviews
CREATE TABLE Reviews (
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
insert into Reviews
SELECT review.* FROM

OPENROWSET(
	BULK 'review_x.json', 
	DATA_SOURCE = 'YelpJsonFiles',
	SINGLE_CLOB
) AS json
CROSS APPLY OPENJSON(BulkColumn)
WITH( 
	review_id nvarchar(100),
	user_id nvarchar(100),
	business_id nvarchar(100),
	stars float,
	date date,
	text nvarchar(max),
	useful int,
	funny int,
	cool int
) as review
;

--------------------------------------------------CHECKIN----------------------------------------------------------------------------
DROP TABLE IF EXISTS Checkins

CREATE TABLE Checkins (
	business_id nvarchar(100),
	date nvarchar(max)  -- list of date in csv format
)

insert into Checkins
SELECT checkin.* FROM

OPENROWSET(
	BULK 'checkin_x.json', 
	DATA_SOURCE = 'YelpJsonFiles',
	SINGLE_CLOB
) AS json
CROSS APPLY OPENJSON(BulkColumn)
 WITH(
	 business_id nvarchar(100),
	 date nvarchar(max)
) as checkin
;
---------------------------------------------------------TIP------------------------------------------------------------
DROP TABLE IF EXISTS Tips
CREATE TABLE Tips (
	business_id nvarchar(100),
	user_id nvarchar(100),
	date date,  -- list of date in csv format
	text nvarchar(max),
	compliment_count int,
	)
insert into Tips
SELECT tip.* FROM

OPENROWSET(
	BULK 'tip_x.json', 
	DATA_SOURCE = 'YelpJsonFiles',
	SINGLE_CLOB
) AS json
CROSS APPLY OPENJSON(BulkColumn)
 WITH(
	business_id nvarchar(100),
	user_id nvarchar(100),
	date date,  -- list of date in csv format
	text nvarchar(max),
	compliment_count int
) as tip
----------------------------------------------------PHOTO----------------------------------------------------------------------

DROP TABLE IF EXISTS Photos
CREATE TABLE Photos (
		photo_id nvarchar(100),
		business_id nvarchar(100),
		caption nvarchar(200),
		label nvarchar(100)
		)

insert into Photos
SELECT photo.* FROM

OPENROWSET(
	BULK 'photo_x.json', 
	DATA_SOURCE = 'YelpJsonFiles',
	SINGLE_CLOB
) AS json
CROSS APPLY OPENJSON(BulkColumn)
 WITH(	photo_id nvarchar(100),
		business_id nvarchar(100),
		caption nvarchar(200),
		label nvarchar(100)
) as photo