-- 1. Create a database called EXERCISE_DB

CREATE DATABASE EXERCISE_DB;

-- 2. Create a table called CUSTOMERS
/*Set the column names and data types as follows:
ID INT,
first_name varchar,
last_name varchar,
email varchar,
age int,
city varchar*/

CREATE TABLE EXERCISE_DB.PUBLIC.CUSTOMERS(
ID INT,
FIRST_NAME VARCHAR(225),
LAST_NAME VARCHAR(225),
EMAIL VARCHAR(50),
AGE INT,
CITY VARCHAR(50)
);

-- 3. Load the data in the table

/*The data is available under: s3://snowflake-assignments-mc/gettingstarted/customers.csv.
Data type: CSV - delimited by ',' (comma)
Header is in the first line.*/

COPY INTO EXERCISE_DB.PUBLIC.CUSTOMERS
FROM 's3://snowflake-assignments-mc/gettingstarted/customers.csv'
FILE_FORMAT = (type = csv
                field_delimiter = ','
                skip_header = 1);


SELECT * FROM EXERCISE_DB.PUBLIC.CUSTOMERS;
