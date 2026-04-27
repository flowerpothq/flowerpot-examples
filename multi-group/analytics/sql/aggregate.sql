DELETE FROM events_summary;

INSERT INTO events_summary
SELECT
    event,
    COUNT(*)    AS cnt,
    SUM(amount) AS total
FROM read_json_auto('../data/normalized/events_clean.json')
GROUP BY event
ORDER BY cnt DESC;

SELECT * FROM events_summary;
