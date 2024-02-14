-- lists all cities contained in the database
-- Query to list cities with corresponding state names
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

