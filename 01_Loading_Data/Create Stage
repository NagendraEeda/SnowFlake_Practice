// Database to manage stage objects, fileformats etc.

CREATE OR REPLACE DATABASE MANAGE_DB;

CREATE OR REPLACE SCHEMA external_stages;

// Creating external stage

CREATE OR REPLACE STAGE MANAGE_DB.EXTERNAL_STAGES.AWS_STAGE
URL = 's3://bucketsnowflakes3'
credentials=(aws_key_id='*****' aws_secret_key='e6mNpF4Z/QTmXQjeWgjfAQn+i1k/xuv4yBfqzXfk');

// Alter external stage   

ALTER STAGE aws_stage
    SET url = 's3://snowflaketestingbuckets3';
    

// Description of external stage

DESC STAGE MANAGE_DB.external_stages.aws_stage; 


// Publicly accessible staging area    

CREATE OR REPLACE STAGE MANAGE_DB.external_stages.aws_stage
    url='s3://bucketsnowflakes3';

// List files in stage

LIST @aws_stage;
