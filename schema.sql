-- Create database (run this in PostgreSQL superuser mode)
-- CREATE DATABASE studentdb;

-- Create sales table
CREATE TABLE IF NOT EXISTS sales (
    order_id INT PRIMARY KEY,
    customer VARCHAR(255),
    product VARCHAR(255),
    quantity INT,
    price INT,
    date DATE,
    total INT
);

-- Create index on date for faster queries
CREATE INDEX IF NOT EXISTS idx_sales_date ON sales(date);

CREATE INDEX IF NOT EXISTS idx_sales_customer ON sales(customer);



---------------------------------------------------- IMPORTANT NOTE ----------------------------------------------------

The above SQL commands are meant to be run in a PostgreSQL database environment. Make sure to replace 'studentdb' with the actual name of your database when creating it. The table 'sales' will be created if it does not already exist, and indexes will be created on the 'date' and 'customer' columns for improved query performance but I have already created the database and table in the etc-script.py file so you can ignore this file.