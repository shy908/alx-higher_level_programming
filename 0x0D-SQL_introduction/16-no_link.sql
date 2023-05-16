-- lists all records of the table second_table having a name value.
-- Records are orderd by descending score.
SELECT `score`, `name`
FROM `second_score`
WHERE `name` != ""
ORDER BY `score` DESC;
