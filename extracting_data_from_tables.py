# Task 2, Joining the tables and extracting the data from those tables


import psycopg2 as connector
from psycopg2 import Error
from config import DB_CONFIG

try:
    connection = connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    access_view = """SELECT C."CustomerID", O."OrderID", M."Name" FROM "Customers" C JOIN "Orders" O ON C."CustomerID" = O."CustomerID" JOIN "Menu" M ON O."MenuID" = M."MenuID";"""
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