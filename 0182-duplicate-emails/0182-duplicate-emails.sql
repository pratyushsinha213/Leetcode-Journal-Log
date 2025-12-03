# Write your MySQL query statement below
SELECT DISTINCT email
FROM (
    SELECT 
        email,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY email) AS rn
    FROM Person
) AS t
WHERE t.rn > 1;