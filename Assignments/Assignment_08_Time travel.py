---> Create exercise table

-- Switch to role of accountadmin --
 
USE ROLE ACCOUNTADMIN;
CREATE OR REPLACE DATABASE DEMO_DB;
USE DATABASE DEMO_DB;
USE WAREHOUSE COMPUTE_WH;
 
CREATE OR REPLACE TABLE DEMO_DB.PUBLIC.PART
AS
SELECT * FROM "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF1"."PART";
 
SELECT * FROM PART
ORDER BY P_MFGR DESC;


---> Update the table

UPDATE DEMO_DB.PUBLIC.PART
SET P_MFGR='Manufacturer#CompanyX'
WHERE P_MFGR='Manufacturer#5';
 
----> Note down query id here:
 
SELECT * FROM PART
ORDER BY P_MFGR DESC;


---> Travel back using the offset until you get the result of before the update

SELECT * FROM DEMO_DB.PUBLIC.PART AT (OFFSET => -60*0.5);


---> Travel back using the query id to get the result before the update

SELECT * FROM DEMO_DB.PUBLIC.PART BEFORE (STATEMENT => '01bb91fb-3201-890e-000c-a6460003d17a')
