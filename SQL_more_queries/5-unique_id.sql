-- Creates the table 'unique_id' if it doesn't already exist
-- Column 'id' must be unique and has a default value of 1
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
