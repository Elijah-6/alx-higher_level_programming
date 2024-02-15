-- list all the cities in california
SELECT id, name FROM `cities`
WHERE cities.state_id = (
	SELECT id FROM `states`
	WHERE name = "California")
ORDER BY id;

