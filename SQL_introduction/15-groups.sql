-- Groups records by score and counts them, ordered by count descending
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
