-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table 'cities' referencing 'states'
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
