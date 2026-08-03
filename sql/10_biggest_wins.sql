USE football_analytics;

SELECT

match_datetime,

competition,

home_team,

away_team,

home_score,

away_score,

ABS(home_score-away_score) AS goal_margin

FROM matches

ORDER BY goal_margin DESC

LIMIT 20;