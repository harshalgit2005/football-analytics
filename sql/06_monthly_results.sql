USE football_analytics;

SELECT

    year,

    month_name,

    COUNT(*) AS matches,

    SUM(home_score) AS home_goals,

    SUM(away_score) AS away_goals,

    SUM(home_score + away_score) AS total_goals

FROM matches

GROUP BY
    year,
    month,
    month_name

ORDER BY
    year,
    month;