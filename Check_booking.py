## Creating a procedure to check the booking id if it exists or not in the table.
# In postgresql, there is no stored procedure, instead it have a function, so creaing a function.

import psycopg2 

from psycopg2 import Error
from config import DB_CONFIG

try:
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()

    #Begin the TRANSACTION
    cursor.execute("BEGIN;")

    # Drop the procedure if it exists (optional)
    drop_proc_query = """DROP FUNCTION IF EXISTS checkbooking(customer_id Integer) CASCADE"""
    cursor.execute(drop_proc_query)
    connection.commit()  # Commit drop procedure


    #creating a function checkbooking which accepts a parameter
    check_proc_query = """CREATE OR REPLACE FUNCTION checkbooking(customer_id INTEGER)      
    RETURNS TABLE(BookingID INTEGER,
        Bill Numeric,
        TableNumber INTEGER,
        Discount NUMERIC,
        Tax NUMERIC,
        CustomerID INTEGER,
        MenuID INTEGER,
        DeliveryID INTEGER
    ) AS $$
    BEGIN
        RETURN QUERY SELECT * FROM "Bookings" WHERE "CustomerID" = checkbooking.customer_id;
    END;
    $$
    LANGUAGE plpgsql;"""

    cursor.execute(check_proc_query)
    customer_id = 3

    cursor.execute("SELECT * FROM checkbooking(%s)",(customer_id,))     # calling checkbooking function with a parameter
    # cols = [desc[0] for desc in cursor.description]
    # print(cols)
    results = cursor.fetchall()
    #print(results)
    for i in results:
        print(i)

    #Transaction commit
    connection.commit()
except psycopg2.DatabaseError as e:
    connection.rollback()
    print(f"Error: {e}")
    print(f"Transaction rolled back: {e}")
     
finally:
     connection.close()