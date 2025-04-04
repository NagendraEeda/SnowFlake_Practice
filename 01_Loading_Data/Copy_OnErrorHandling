// Creating ORDERS ER table

CREATE OR REPLACE TABLE OUR_FIRST_DB.PUBLIC.ORDERS_ER (
    ORDER_ID VARCHAR(30),
    AMOUNT INT,
    PROFIT INT,
    QUANTITY INT,
    CATEGORY VARCHAR(30),
    SUBCATEGORY VARCHAR(30));

    
CREATE OR REPLACE STAGE MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE_ERROREX
URL = 's3://bucketsnowflakes3'
credentials = (aws_key_id = '*******' aws_secret_key='e6mNpF4Z/QTmXQjeWgjfAQn+i1k/xuv4yBfqzXfk');

LIST @MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE_ERROREX;

ALTER STAGE MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE_ERROREX
SET URL = 's3://snowflaketestingbuckets3';

SELECT * FROM OUR_FIRST_DB.PUBLIC.ORDERS_ER;
TRUNCATE TABLE OUR_FIRST_DB.PUBLIC.ORDERS_ER;

-- the below statement will throw and error beacuse of we are loading string values instead of int in one of the field

COPY INTO OUR_FIRST_DB.PUBLIC.ORDERS_ER
FROM @MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE_ERROREX
file_format = (type = csv field_delimiter = ',' skip_header = 1)
pattern = ".*Error.*";


-- it exclude the error records and insert remaining

COPY INTO OUR_FIRST_DB.PUBLIC.ORDERS_ER
FROM @MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE_ERROREX
file_format = (type = csv field_delimiter = ',' skip_header = 1)
pattern = ".*Error.*"
ON_ERROR = 'CONTINUE';


-- it skip entire file if it having one error record.

COPY INTO OUR_FIRST_DB.PUBLIC.ORDERS_ER
FROM @MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE_ERROREX
file_format = (type = csv field_delimiter = ',' skip_header = 1)
pattern = ".*Error.*"
ON_ERROR = 'SKIP_FILE';


-- it skip entire file if it having more than or equal two error records.

COPY INTO OUR_FIRST_DB.PUBLIC.ORDERS_ER
FROM @MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE_ERROREX
file_format = (type = csv field_delimiter = ',' skip_header = 1)
pattern = ".*Error.*"
ON_ERROR = 'SKIP_FILE_2';


-- we can also use the percentage on error handing

COPY INTO OUR_FIRST_DB.PUBLIC.ORDERS_ER
FROM @MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE_ERROREX
file_format = (type = csv field_delimiter = ',' skip_header = 1)
pattern = ".*Error.*"
ON_ERROR = 'SKIP_FILE_2%';
