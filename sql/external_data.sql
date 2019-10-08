-- Create encryption password
CREATE MASTER KEY ENCRYPTION BY PASSWORD='{mssql_master_password}';

-- Delete credential
DROP DATABASE SCOPED CREDENTIAL AppCred

-- Create a database scoped credential.
CREATE DATABASE SCOPED CREDENTIAL AppCred 
WITH 
	IDENTITY = 'SHARED ACCESS SIGNATURE',
    SECRET = '{blob_sas_token}';
;

-- Create external data source using credential
CREATE EXTERNAL DATA SOURCE YelpJsonFiles
    WITH (
        TYPE = BLOB_STORAGE,
        LOCATION = 'https://yelpjson.blob.core.windows.net/raw',
        CREDENTIAL = AppCred
    );