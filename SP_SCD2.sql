CREATE OR REPLACE PROCEDURE TRAINING.DISTRIBUTION.PROCESS_SCD2_UPDATE()
RETURNS STRING
LANGUAGE SQL
AS
$$
BEGIN
    -- Drop Temporary Table If It Exists
    DROP TABLE IF EXISTS DISTRIBUTION.TEMP_SCD2;

    -- Create Temporary Table for Latest Customer Data
    CREATE TEMPORARY TABLE DISTRIBUTION.TEMP_SCD2 AS
    SELECT * FROM EXTRACTION.STG_CUSTOMER_SCD
    WHERE DT_INSERT = (SELECT MAX(DT_INSERT) FROM EXTRACTION.STG_CUSTOMER_SCD);

    -- Insert New Customers (Only If They Don't Exist)
    INSERT INTO DISTRIBUTION.DST_CUSTOMER_SCD2 (customer_id, customer_name, customer_address, start_date, end_date, status)
    SELECT S.customer_id, S.customer_name, S.customer_address, CURRENT_TIMESTAMP, NULL, 'Y'
    FROM DISTRIBUTION.TEMP_SCD2 S
    WHERE NOT EXISTS (
        SELECT 1 FROM DISTRIBUTION.DST_CUSTOMER_SCD2 T
        WHERE T.customer_id = S.customer_id
        AND T.status = 'Y'
    );

    -- Expire Existing Records (Only If Name or Address Has Changed)
    UPDATE DISTRIBUTION.DST_CUSTOMER_SCD2 
    SET end_date = CURRENT_TIMESTAMP, status = 'N'
    WHERE customer_id IN (
        SELECT DISTINCT B.customer_id 
        FROM DISTRIBUTION.TEMP_SCD2 A
        JOIN DISTRIBUTION.DST_CUSTOMER_SCD2 B
        ON A.customer_id = B.customer_id
        WHERE (A.customer_name <> B.customer_name OR A.customer_address <> B.customer_address)
        AND B.status = 'Y'
    );

    -- Insert New Version of Updated Records (Only If Not Already Inserted)
    INSERT INTO DISTRIBUTION.DST_CUSTOMER_SCD2 (customer_id, customer_name, customer_address, start_date, end_date, status)
    SELECT A.customer_id, A.customer_name, A.customer_address, CURRENT_TIMESTAMP, NULL, 'Y'
    FROM DISTRIBUTION.TEMP_SCD2 A
    JOIN (
        SELECT customer_id, MAX(start_date) AS latest_start_date
        FROM DISTRIBUTION.DST_CUSTOMER_SCD2
        WHERE status = 'N'
        GROUP BY customer_id
    ) B
    ON A.customer_id = B.customer_id
    WHERE NOT EXISTS ( -- Prevent duplicate inserts
        SELECT 1 FROM DISTRIBUTION.DST_CUSTOMER_SCD2 C
        WHERE C.customer_id = A.customer_id
        AND C.customer_name = A.customer_name
        AND C.customer_address = A.customer_address
        AND C.status = 'Y'
    );

    -- Drop Temporary Table
    DROP TABLE IF EXISTS DISTRIBUTION.TEMP_SCD2;

    RETURN 'SCD Type 2 Processing Completed Successfully';
END;
$$;
