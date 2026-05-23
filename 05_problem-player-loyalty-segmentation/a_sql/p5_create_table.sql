DROP TABLE IF EXISTS p5_player_loyalty_raw;

CREATE TABLE p5_player_loyalty_raw (
    player_id INTEGER,
    player_name VARCHAR(100),
    age INTEGER,
    state VARCHAR(10),
    visits INTEGER,
    theoretical_win NUMERIC(12,2),
    actual_win NUMERIC(12,2),
    loyalty_tier VARCHAR(20)
);
