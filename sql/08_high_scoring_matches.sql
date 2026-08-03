USE football_analytics;

SELECT

    match_datetime,

    competition,

    home_team,

    away_team,

    home_score,

    away_score,

    home_score + away_score AS total_goals

FROM matches

ORDER BY total_goals DESC

LIMIT 20;