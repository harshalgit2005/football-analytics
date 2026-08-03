USE football_analytics;

SELECT
    league,
    position,
    team_name,
    played_games,
    won,
    draw,
    lost,
    goals_for,
    goals_against,
    goal_difference,
    points
FROM standings
ORDER BY
    league,
    position;