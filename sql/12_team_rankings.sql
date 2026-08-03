USE football_analytics;

SELECT

league,

team_name,

points,

RANK() OVER(

PARTITION BY league

ORDER BY points DESC

) AS league_rank

FROM standings;