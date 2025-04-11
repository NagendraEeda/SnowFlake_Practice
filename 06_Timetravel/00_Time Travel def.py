Query the historic data within in the retention time

Ways to retrive the data
---------------------------

1. TimeStamp

    SELECT * FROM TABLE AT (TIMESTAMP => timestamp);
    
2. Offset

   SELECT * FROM TABLE AT (OFFSET => -10*60);
   
3. Query

   SELECT * FROM TABLE AT (statement => query_id);


*********************************************************************

Recover the objects that have been dropped within rentention period

undrop TABLE table_name;
undrop schema schema_name;
undrop  database database_name;

