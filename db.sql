-- Switch to the database
create database flask_real;
USE flask_real;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS sell;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS buy;
DROP TABLE IF EXISTS complaints;
DROP TABLE IF EXISTS my_properties;  -- Added my_properties table
DROP PROCEDURE IF EXISTS AddUser;

-- Alter user password
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your password';
FLUSH PRIVILEGES;

-- Set session variables
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

-- Create table for sell properties
CREATE TABLE sell (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property_name VARCHAR(255),
    address TEXT,
    price varchar(150)
);

-- Create table for users (Registration & Login)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Insert initial user credentials
INSERT INTO users (username, password) VALUES 
('admin', '123'),
('student1', 'pass1'),
('student2', 'pass2');

-- Create table for buy properties
CREATE TABLE buy (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    price Varchar(150) NOT NULL
);

-- Insert sample data for buy table
INSERT INTO buy (property_name, address, price) 
VALUES 
("Prestige Lakeside Habitat", "Whitefield, Bengaluru", 12000000),
("Brigade Exotica", "Old Madras Road, Bengaluru", 8500000),
("Sobha Dream Acres", "Panathur, Bengaluru", 9500000),
("Godrej Woodland", "Sarjapur, Bengaluru", 7800000),
("Purva Palm Beach", "Hennur Road, Bengaluru", 15000000),
("Prestige Golfshire", "Devanahalli, Bengaluru", 11000000),
("Brigade El Dorado", "Bagalur, Bengaluru", 9200000),
("RMZ Galleria", "Yelahanka, Bengaluru", 6500000),
("Vaishnavi Oasis", "JP Nagar, Bengaluru", 9800000),
("Mantri Serenity", "Kanakapura Road, Bengaluru", 12500000),
("Nitesh Park Avenue", "Sankey Road, Bengaluru", 8900000),
("Sobha Forest View", "Kanakapura Road, Bengaluru", 8000000),
("Rohan Upavan", "Hennur, Bengaluru", 9400000),
("Adarsh Palm Retreat", "Bellandur, Bengaluru", 13000000),
("Purva Atmosphere", "Thanisandra Main Road, Bengaluru", 7100000),
("Embassy Boulevard", "North Bengaluru", 8400000),
("Salarpuria Sattva Divinity", "Mysore Road, Bengaluru", 9900000),
("Mahaveer Ranches", "Sarjapur Road, Bengaluru", 10500000),
("Total Environment Pursuit", "Whitefield, Bengaluru", 11000000),
("Kolte Patil Mirabilis", "Horamavu, Bengaluru", 12000000);

-- Create table for complaints
CREATE TABLE complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255) NOT NULL,
    complaint TEXT NOT NULL
);

-- Insert sample complaints
INSERT INTO complaints (username, contact_info, complaint) 
VALUES 
('student1', 'student1@example.com', 'Unable to access the buy properties.'),
('student2', 'student2@example.com', 'Issue with property listing display.'),
('admin', 'admin@example.com', 'Problem with login authentication.');

-- Create table for my_properties
CREATE TABLE my_properties (
    id INT NOT NULL AUTO_INCREMENT,
    property_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    price varchar(150) NOT NULL,
    PRIMARY KEY (id)
);

-- Procedure to insert a new user
DELIMITER //
CREATE PROCEDURE AddUser(IN userName VARCHAR(255), IN userPass VARCHAR(255))
BEGIN
    IF NOT EXISTS (SELECT * FROM users WHERE username = userName) THEN
        INSERT INTO users (username, password) VALUES (userName, userPass);
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Username already exists.';
    END IF;
END //
DELIMITER ;

-- Nested query to find the most expensive property available in buy table
SELECT property_name, price
FROM buy
WHERE price = (SELECT MAX(price) FROM buy);

-- Join query to show complaints with user details (username) and property-related issues
SELECT c.username, c.contact_info, c.complaint, b.property_name
FROM complaints c
LEFT JOIN buy b ON c.username = 'student1' OR c.username = 'student2';

-- Aggregate query to calculate average property price in buy table
SELECT AVG(price) AS average_price
FROM buy;

-- Commit the transaction

COMMIT;
