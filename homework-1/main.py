"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


with psycopg2.connect(host='localhost',database='north',user='postgres',password='Komaz5357abv') as conn:
    
   with conn.cursor() as cur:

      cur = conn.cursor()
      with open('homework-1/north_data/employees_data.csv', 'r') as f:
         reader = csv.reader(f)
         next(reader)
         for row in reader:
            cur.execute(
               "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5])
            )
            

   with conn.cursor() as cur:

      cur = conn.cursor()
      with open('homework-1/north_data/customers_data.csv', 'r') as f:
         reader = csv.reader(f)
         next(reader)
         for row in reader:
            cur.execute(
               "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
            (row[0], row[1], row[2])
            )

   with conn.cursor() as cur:

      cur = conn.cursor()
      with open('homework-1/north_data/orders_data.csv', 'r') as f:
         reader = csv.reader(f)
         next(reader)
         for row in reader:
            cur.execute(
               "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4])
            )

conn.commit()
conn.close()

