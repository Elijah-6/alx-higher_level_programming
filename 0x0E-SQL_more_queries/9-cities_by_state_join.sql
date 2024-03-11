-- lists all cities contained in the database
-- Query to list cities with corresponding state names
-- Records are sorted in order of ascending cities.id.
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
