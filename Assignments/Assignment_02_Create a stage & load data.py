SELECT * FROM EXERCISE_DB.PUBLIC.CUSTOMERS;

TRUNCATE TABLE EXERCISE_DB.PUBLIC.CUSTOMERS;

//create stage

CREATE OR REPLACE STAGE MANAGE_DB.EXTERNAL_STAGES.aws_stage2
url = 's3://snowflake-assignments-mc/loadingdata/';

LIST @MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE2;

COPY INTO EXERCISE_DB.PUBLIC.CUSTOMERS
FROM @MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE2
FILE_FORMAT = (type = csv
                field_delimiter = ';'
                skip_header = 1)
                pattern = '.*customers.*';



 ---- Assignment solution - Create stage & load data ----
 
-- create stage object
CREATE OR REPLACE STAGE EXERCISE_DB.public.aws_stage
    url='s3://snowflake-assignments-mc/loadingdata';

-- List files in stage
LIST @EXERCISE_DB.public.aws_stage;

-- Load the data 
COPY INTO EXERCISE_DB.PUBLIC.CUSTOMERS
    FROM @aws_stage
    file_format= (type = csv field_delimiter=';' skip_header=1)
