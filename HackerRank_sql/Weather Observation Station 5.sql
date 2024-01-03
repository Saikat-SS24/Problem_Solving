/* Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths 
(i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes 
first when ordered alphabetically.
The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.

Sample Input

For example, CITY has four entries: DEF, ABC, PQRS and WXY.

Sample Output

ABC 3
PQRS 4
Explanation

When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths  and . The longest name 
is PQRS, but there are  options for shortest named city. Choose ABC, because it comes first alphabetically.

Note
You can write two separate queries to get the desired output. It need not be a single query. */

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CITY || ' ' || LENGTH 
FROM (
SELECT CITY , LENGTH(CITY) AS LENGTH
FROM STATION 
WHERE LENGTH(CITY) = (SELECT MAX(LENGTH(CITY)) FROM STATION) 
ORDER BY CITY ) 
WHERE ROWNUM <= 1
UNION
SELECT CITY || ' ' || LENGTH 
FROM (
SELECT CITY , LENGTH(CITY) AS LENGTH
FROM STATION 
WHERE LENGTH(CITY) = (SELECT MIN(LENGTH(CITY)) FROM STATION) 
ORDER BY CITY ) 
WHERE ROWNUM <= 1 ;