import psycopg2 as connector
from psycopg2 import Error, sql
from faker import Faker
import numpy as np
import pandas as pd


#connecting to the database
try:
    connection = connector.connect(host = "localhost", dbname="LittleLemonDB", user="postgres", password="Bhaktapur@2024" )
    cursor = connection.cursor()

    query ="""SELECT *
    FROM information_schema.tables
    WHERE table_schema = 'public';
    """
    cursor.execute(query)
    tables = cursor.fetchall()
    for table in tables:
        print(table)


except Error as e:
    print(f"Error: {e}")
    print("Try again.")
    
if connection:
    cursor.close()
    connection.close()