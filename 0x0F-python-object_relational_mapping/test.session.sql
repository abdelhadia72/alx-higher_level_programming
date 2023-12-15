--@block
SELECT cities.id,
    cities.name AS city,
    states.name AS state
FROM cities
    INNER JOIN states ON cities.state_id = state_id
ORDER BY cities.name ASC;