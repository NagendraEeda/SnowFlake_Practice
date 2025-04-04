SELECT * FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;

// Second step: Parse & Analyse Raw JSON 

// Selecting attribute/column

SELECT RAW:city FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;

SELECT $1:first_name FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;


// Selecting attribute/column - formattted

SELECT RAW:first_name::string as first_name  FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;

SELECT RAW:id::int as id  FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;

SELECT 
    RAW:id::int as id,  
    RAW:first_name::STRING as first_name,
    RAW:last_name::STRING as last_name,
    RAW:gender::STRING as gender

FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;



   // Handling nested data
   
SELECT RAW:job as job  FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;



SELECT * FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;

-- Nested values under job 

SELECT 
    RAW:id::int as id,  
    RAW:job.salary::int as salary,
    RAW:job.title::STRING as title
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;
