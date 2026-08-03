USE football_analytics;

SELECT

    home_team,

    COUNT(*) AS matches,

    SUM(home_score) AS goals,

    AVG(home_score) AS avg_goals,

    SUM(
        CASE
            WHEN winner='HOME_TEAM'
            THEN 1
            ELSE 0
        END
    ) AS home_wins

FROM matches

GROUP BY home_team

ORDER BY home_wins DESC;