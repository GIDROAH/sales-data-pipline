SELECT * FROM sales;

SELECT customer, SUM(total) AS total_earned
FROM sales
GROUP BY customer;

SELECT product, SUM(quantity) AS total_sold
FROM sales
GROUP BY product;