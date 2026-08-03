USE football_analytics;

SELECT
    team_name,
    league,
    points,
    won,
    draw,
    lost,
    goal_difference
FROM standings
ORDER BY
    points DESC,
    goal_difference DESC
LIMIT 10;