USE football_analytics;

SELECT

team_name,

league,

goal_difference,

points

FROM standings

ORDER BY goal_difference DESC;