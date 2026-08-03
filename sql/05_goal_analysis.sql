USE football_analytics;

SELECT

    competition,

    COUNT(*) AS total_matches,

    SUM(home_score + away_score) AS total_goals,

    ROUND(
        AVG(home_score + away_score),
        2
    ) AS avg_goals

FROM matches

GROUP BY competition

ORDER BY avg_goals DESC;