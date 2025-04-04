SELECT * FROM EXERCISE_DB.PUBLIC.JSON_RAW;


/*2. Select the attributes
first_name
last_name
skills
and query these columns.*/


SELECT 
RAW:first_name:: STRING AS FIRST_NAME,
RAW:last_name:: STRING AS LAST_NAME,
RAW:Skills
FROM EXERCISE_DB.PUBLIC.JSON_RAW;


/*2. The skills column contains an array. Query the first two values in the skills attribute for every record in a separate column:
first_name
last_name
skills_1
skills_2*/

SELECT 
$1:first_name:: STRING AS FIRST_NAME,
$1:last_name:: STRING AS LAST_NAME,
$1:Skills[0]:: STRING AS SKILL_1,
$1:Skills[1]:: STRING AS SKILL_2
FROM EXERCISE_DB.PUBLIC.JSON_RAW;

/*3.Create a table and insert the data for these 4 columns in that table.*/

CREATE OR REPLACE TABLE EXERCISE_DB.PUBLIC.JSON_PARSED AS
SELECT 
$1:first_name:: STRING AS FIRST_NAME,
$1:last_name:: STRING AS LAST_NAME,
$1:Skills[0]:: STRING AS SKILL_1,
$1:Skills[1]:: STRING AS SKILL_2
FROM EXERCISE_DB.PUBLIC.JSON_RAW;

SELECT * FROM EXERCISE_DB.PUBLIC.JSON_PARSED;
