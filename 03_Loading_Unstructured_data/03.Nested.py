SELECT * FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;

-- Nested values under job 

SELECT 
    RAW:id::int as id,  
    RAW:job.salary::int as salary,
    RAW:job.title::STRING as title
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;
