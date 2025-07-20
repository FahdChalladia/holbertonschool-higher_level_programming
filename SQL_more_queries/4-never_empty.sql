-- Creates the table 'id_not_null' if it doesn't already exist
-- Column 'id' defaults to 1 if not specified
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
