/* Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result 
cannot contain duplicates.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude. */


/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select 
    t.Field 
    From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
SELECT DISTINCT CITY
FROM STATION
WHERE (NOT(CITY  Like 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'O%' OR CITY LIKE 'I%' OR CITY LIKE 'U%'))
        OR 
      (NOT (CITY LIKE '%a' OR CITY  LIKE '%e' OR CITY LIKE '%i' OR CITY LIKE '%o' OR CITY LIKE '%u'))
ORDER BY CITY;