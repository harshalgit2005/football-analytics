USE football_analytics;

-- Total Matches
SELECT COUNT(*) AS total_matches
FROM matches;

-- Total Teams
SELECT COUNT(*) AS total_teams
FROM teams;

-- Total Goals
SELECT SUM(home_score+away_score) AS total_goals
FROM matches;

-- Average Goals
SELECT ROUND(AVG(home_score+away_score),2) AS avg_goals
FROM matches;

-- Total Competitions
SELECT COUNT(DISTINCT competition) AS competitions
FROM matches;