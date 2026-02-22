### Sales Data Pipeline (Python + PostgreSQL)

### 📌 Overview
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python and PostgreSQL.  
It ingests raw sales data from CSV files, cleans and transforms it in Python, loads it into a PostgreSQL database, and finally runs SQL queries to generate business insights such as total revenue, top products, and monthly sales trends.


### 🛠 Tech Stack
1. Python (Pandas, psycopg2)
2. PostgreSQL
3. SQL


### 🔄 Project Workflow
1. **Extract** → Read sales data from CSV using Python.  
2. **Transform** → Clean data, calculate `total = quantity * price`.  
3. **Load** → Insert transformed data into PostgreSQL.  
4. **Query** → Run SQL queries to generate insights.


### ⚙️ Setup Instructions
1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sales-data-pipeline.git
   cd sales-data-pipeline

   python scripts/etl.py

   psql -U postgres -d studentdb -f sql/queries.sql // if you don't have then only run this.

2. Step-by-step so anyone can run it:

1. Clone the repo
2. Install dependencies: pip install -r requirements.txt
3. Create PostgreSQL database: studentdb
4. Run schema.sql to create tables
5. Run etl.py to load data
6. Run queries.sql for insights


----------------------------------------------------- Some Outputs -----------------------------------------------------

### Terminal Output
```bash
(.venv) PS D:\Deepak\data_engineer\sales-data-pipline> python etl-script.py
Enter your database name: studentdb
Enter your database password: [password]
Database connection successful!
Data inserted successfully!
```

### Postgres Output
```sql
studentdb=# select * from sales;

 order_id | customer | product | quantity | price |    date    | total
----------+----------+---------+----------+-------+------------+-------
        1 | Deepak   | Laptop  |        1 | 60000 | 2026-01-10 | 60000
        2 | Ravi     | Phone   |        2 | 15000 | 2026-01-12 | 30000
        3 | Anita    | Tablet  |        1 | 25000 | 2026-01-15 | 25000
        4 | Rahul    | Laptop  |        1 | 60000 | 2026-01-20 | 60000
        5 | Sunita   | Phone   |        1 | 15000 | 2026-01-25 | 15000
        6 | Mannu    | RAM     |        2 |  8000 | 2026-02-22 | 16000
(6 rows)
```
```
studentdb=# SELECT product, SUM(quantity) AS total_sold
studentdb-# FROM sales
studentdb-# GROUP BY product;

 product | total_sold
---------+------------
 Tablet  |          1
 Phone   |          3
 RAM     |          2
 Laptop  |          2
(4 rows)


studentdb=# SELECT customer, SUM(total) AS total_earned
studentdb-# FROM sales
studentdb-# GROUP BY customer

 customer | total_earned
----------+--------------
 Rahul    |        60000
 Ravi     |        30000
 Mannu    |        16000
 Deepak   |        60000
 Sunita   |        15000
 Anita    |        25000
(6 rows)

```
-------------------------------------------------- Future Improvement ------------------------------------------------- 


### Project Structure
    │
    ├── data/
    │   └── sales.csv
    │
    ├── scripts/
    │   └── etl.py
    │
    ├── sql/
    │   ├── schema.sql
    │   └── queries.sql
    │
    ├── README.md
    └── requirements.txt
```
