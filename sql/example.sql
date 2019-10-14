-- Openrowset
SELECT * FROM OPENROWSET(
   BULK 'business_x.csv',
   DATA_SOURCE = 'YelpJsonFiles',
   --FORMAT = 'JSON',
   SINGLE_CLOB
   ) AS DataFile
;

-- Bulk Insert
BEGIN
   BULK INSERT Businesses2
   FROM 'business_x.csv'
   WITH (
      FORMAT = 'CSV',
      DATA_SOURCE = 'YelpJsonFiles',
      FIELDTERMINATOR = ','
   )
   ;
END

-- Get a list of databases
SELECT name FROM sys.databases
GO