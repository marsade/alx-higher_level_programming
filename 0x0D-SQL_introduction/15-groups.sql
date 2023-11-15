-- Lists the number of records with the same score in second_table
SELECT `score`, COUNT(`score`) AS numbers
FROM `second_table`
GROUP BY `score`
ORDER BY `score` DESC
