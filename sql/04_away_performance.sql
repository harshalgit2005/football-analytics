USE football_analytics;

SELECT

    away_team,

    COUNT(*) AS matches,

    SUM(away_score) AS goals,

    AVG(away_score) AS avg_goals,

    SUM(
        CASE
            WHEN winner='AWAY_TEAM'
            THEN 1
            ELSE 0
        END
    ) AS away_wins

FROM matches

GROUP BY away_team

ORDER BY away_wins DESC;