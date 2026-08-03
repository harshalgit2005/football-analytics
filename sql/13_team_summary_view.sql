USE football_analytics;

CREATE OR REPLACE VIEW vw_team_summary AS

SELECT

t.team_name,

t.country,

s.league,

s.position,

s.points,

s.goal_difference,

s.form

FROM teams t

INNER JOIN standings s

ON t.team_id=s.team_id;