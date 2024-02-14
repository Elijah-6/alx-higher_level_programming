-- list all the cities in california
USE hbtn_0d_usa;
SELECT * FROM `cities`
WHERE cities.state_id = (
	SELECT id FROM states
	WHERE name = "California")
ORDER BY cities.id;

