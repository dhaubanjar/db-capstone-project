#Chapter 7, module 2, Task 1: In this file, I am trying to create view OrdersView which have some  query with conditions, and I have to use that view to show the tables.


import psycopg2 as connector
from psycopg2 import Error

try:
    connection = connector.connect(host = "localhost", user="postgres", password="Bhaktapur@2024", dbname="LittleLemonDB")
    cursor = connection.cursor()

    view_query = """CREATE VIEW OrdersView AS
    SELECT "OrderID", "OrderTotal"  FROM "Orders" WHERE "OrderTotal" > 800; """

    cursor.execute(view_query)

    access_view = """SELECT * FROM OrdersView;"""
    cursor.execute(access_view)
    results = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]             #Way to access column names in PSQL
    print(colnames)
    for i in results:
        print(i)
except Error as e:
    print(f"Error: {e}")
    print("Try again.")
    
connection.close()