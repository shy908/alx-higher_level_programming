-- Lists the numbr of records with the same scor in th table second_table.
-- Records are ordered by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
