USE football_analytics;

SELECT

competition,

COUNT(*) AS matches,

AVG(home_score) AS avg_home_goals,

AVG(away_score) AS avg_away_goals,

AVG(home_score+away_score) AS avg_total_goals

FROM matches

GROUP BY competition

ORDER BY avg_total_goals DESC;