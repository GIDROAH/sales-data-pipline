import pandas as pd
import psycopg2

data = pd.read_csv('data.csv')
data['total'] = data['quantity'] * data['price']

try:
    conn = psycopg2.connect(
        dbname = input("Enter your database name: "),       # enter the database name eg. -> studentdb
        user = 'postgres',                                  # enter the database username eg. -> postgres
        password =input("Enter your database password: "),  # enter the database password
        host ='localhost',                                  # enter the database host name eg. -> localhost 
        port ='5432'                                        # enter the database port number eg. -> 5432
    )
    print("Database connection successful!")

except Exception as e:
    print(f'Database connection failed: {e}')

cur = conn.cursor()
for _, row in data.iterrows():
    cur.execute("INSERT INTO sales (order_id, customar, product, quantity, price, date, total) values (%s,%s,%s,%s,%s,%s,%s)", (row["order_id"], row["customar"], row["product"], row["quantity"], row["price"], row["date"], row["total"]))
    conn.commit()
cur.close()
conn.close()

print("Data inserted successfully!")