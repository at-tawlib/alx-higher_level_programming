--  creates the table unique_id with a unique id (INT and default value 1) and name (VARCHAR)
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
