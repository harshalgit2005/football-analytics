USE football_analytics;

SELECT

    team_name,

    league,

    form,

    points

FROM standings

ORDER BY
    points DESC;