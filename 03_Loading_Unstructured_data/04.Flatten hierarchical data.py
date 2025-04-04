


SELECT 
    RAW:spoken_languages as spoken_languages
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;

SELECT * FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;


SELECT 
     array_size(RAW:spoken_languages) as spoken_languages
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;


SELECT 
     RAW:first_name::STRING as first_name,
     array_size(RAW:spoken_languages) as spoken_languages
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;



SELECT 
    RAW:spoken_languages[0] as First_language
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;


SELECT 
    RAW:first_name::STRING as first_name,
    RAW:spoken_languages[0] as First_language
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;


SELECT 
    RAW:first_name::STRING as First_name,
    RAW:spoken_languages[0].language::STRING as First_language,
    RAW:spoken_languages[0].level::STRING as Level_spoken
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW;




SELECT 
    RAW:id::int as id,
    RAW:first_name::STRING as First_name,
    RAW:spoken_languages[0].language::STRING as First_language,
    RAW:spoken_languages[0].level::STRING as Level_spoken
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW
UNION ALL 
SELECT 
    RAW:id::int as id,
    RAW:first_name::STRING as First_name,
    RAW:spoken_languages[1].language::STRING as First_language,
    RAW:spoken_languages[1].level::STRING as Level_spoken
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW
UNION ALL 
SELECT 
    RAW:id::int as id,
    RAW:first_name::STRING as First_name,
    RAW:spoken_languages[2].language::STRING as First_language,
    RAW:spoken_languages[2].level::STRING as Level_spoken
FROM OUR_FIRST_DB.PUBLIC.JSON_RAW
ORDER BY ID;




select
      RAW:first_name::STRING as First_name,
    f.value:language::STRING as language,
   f.value:level::STRING as Level_spoken
from OUR_FIRST_DB.PUBLIC.JSON_RAW, table(flatten(RAW:spoken_languages)) f;
