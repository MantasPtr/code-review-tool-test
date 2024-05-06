SELECT user_id AS user, portal AS portal, event_ts, country_code
FROM `some-project.some_dataset.some_table`
WHERE event_ts BETWEEN TIMESTAMP('2024-02-17 00:00:00') AND TIMESTAMP('2024-02-20 00:00:00')
QUALIFY ROW_NUMBER() OVER(
    PARTITION BY user, portal
    ORDER BY event_ts, calc_ts
) = 1