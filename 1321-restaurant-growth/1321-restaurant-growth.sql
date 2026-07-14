# Write your MySQL query statement below
WITH cte1 AS (
SELECT 
SUM(amount) AS daily_total, 
visited_on 
FROM customer 
GROUP BY visited_on 
ORDER BY visited_on
)
SELECT 
d1.visited_on, 
SUM(d2.daily_total) AS amount, 
ROUND(SUM(d2.daily_total) / 7, 2) AS average_amount 
FROM cte1 AS d1 
CROSS JOIN cte1 AS d2 
WHERE d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY) AND d1.visited_on 
GROUP BY d1.visited_on 
HAVING COUNT(d2.visited_on) > 6 
ORDER BY d1.visited_on;