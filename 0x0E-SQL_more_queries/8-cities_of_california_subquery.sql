-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- states table contains one record (California)
-- Results must be sorted in ascending order by cities.id
SELECT * FROM cities 
	WHERE state_id = 
	(SELECT id FROM cities WHERE name = "California");
