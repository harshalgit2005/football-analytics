USE football_analytics;

SELECT

winner,

COUNT(*) AS matches

FROM matches

GROUP BY winner

ORDER BY matches DESC;