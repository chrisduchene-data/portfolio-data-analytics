SELECT
    loyalty_tier,

    COUNT(player_id) AS total_players,

    ROUND(AVG(visits), 1) AS avg_visits,

    ROUND(AVG(theoretical_win), 2) AS avg_theoretical_win,

    ROUND(AVG(actual_win), 2) AS avg_actual_win,

    ROUND(SUM(actual_win), 2) AS total_actual_win

FROM p5_player_loyalty_raw

GROUP BY loyalty_tier

ORDER BY total_actual_win DESC;