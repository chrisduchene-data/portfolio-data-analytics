-- Project 2: Promotional Effectiveness
-- Step 1: Create raw promo table

DROP TABLE IF EXISTS p2_promo_raw;

CREATE TABLE p2_promo_raw (
    promo_date DATE,
    property VARCHAR(50),
    campaign VARCHAR(100),
    channel VARCHAR(50),
    promo_spend NUMERIC(10,2),
    redemptions INTEGER,
    promo_revenue NUMERIC(12,2)
);
