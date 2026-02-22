import pandas as pd
import psycopg2

data = pd.read_csv('data.csv')
data['total'] = data['quantity'] * data['price']

try:
    conn = psycopg2.connect(
        dbname = input("Enter your database name: "),       # enter the database name eg. -> studentdb
        user = 'postgres',                                  # enter the database username eg. -> postgres
        password = input("Enter your database password: "),  # enter the database password
        host ='localhost',                                  # enter the database host name eg. -> localhost 
        port ='5432'                                        # enter the database port number eg. -> 5432
    )
    print("Database connection successful!")

except Exception as e:
    print(f'Database connection failed: {e}')

cur = conn.cursor()

# Create table first (outside the loop)
cur.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        order_id int primary key,
        customer varchar(255),
        product varchar(255),
        quantity int,
        price int,
        date date,
        total int)
""")
conn.commit()

# Then insert data
for _, row in data.iterrows():
    cur.execute("""INSERT INTO sales (order_id, customer, product, quantity, price, date, total) 
                values (%s,%s,%s,%s,%s,%s,%s) 
                ON CONFLICT (order_id) DO UPDATE SET
                customer = EXCLUDED.customer,
                product = EXCLUDED.product,
                quantity = EXCLUDED.quantity,
                price = EXCLUDED.price,
                date = EXCLUDED.date,
                total = EXCLUDED.total""",
                (row["order_id"], 
                 row["customer"], 
                 row["product"], 
                 row["quantity"], 
                 row["price"], 
                 row["date"], 
                 row["total"]))
    conn.commit()
cur.close()
conn.close()

print("Data inserted successfully!")