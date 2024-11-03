/* P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* 
* * 
* * * 
* * * * 
* * * * *
Write a query to print the pattern P(20). */

/*
Enter your query here.
*/

SET @TEMP:=0; SELECT REPEAT('* ', @TEMP:= @TEMP + 1) FROM INFORMATION_SCHEMA.TABLES WHERE @TEMP < 20;