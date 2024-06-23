# Module 2 2nd exercise: Task 3
## Creating a procedure to check the booking id if it exists or not in the table and drop the column if exist to cancel the booking.


import psycopg2 

from psycopg2 import Error
from config import DB_CONFIG

try:
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()

    #Begin the TRANSACTION
    cursor.execute("BEGIN;")

    # Drop the procedure if it exists (optional)
    drop_proc_query = """DROP FUNCTION IF EXISTS checkbooking(table_number INTEGER, booking_date DATE) CASCADE"""
    cursor.execute(drop_proc_query)
    connection.commit()  # Commit drop procedure


    #creating a function checkbooking which accepts a parameter
    check_proc_query = """CREATE OR REPLACE FUNCTION checkbooking(table_number INTEGER, booking_date DATE)      
    RETURNS TABLE(BookingID INTEGER,
        Bill Numeric,
        TableNumber INTEGER,
        Discount NUMERIC,
        Tax NUMERIC,
        CustomerID INTEGER,
        MenuID INTEGER,
        DeliveryID INTEGER,
        BookingDate Date
    ) AS $$
    BEGIN
        RETURN QUERY delete from "Bookings" where "TableNumber" = checkbooking.table_number AND "BookingDate" = checkbooking.booking_date Returning *;
    END;
    $$
    LANGUAGE plpgsql;"""

    cursor.execute(check_proc_query)
    table_number = 6
    booking_date = '2024-07-06'

    cursor.execute("SELECT * FROM checkbooking(%s, %s)",(table_number, booking_date,))     # calling checkbooking function with a parameter
    # cols = [desc[0] for desc in cursor.description]
    # print(cols)
    results = cursor.fetchall()
    if results:
        print(f"Deleted Successfully.")

    else:
        print(f"Nothing happened.")
    

    #Transaction commit
    connection.commit()
except psycopg2.DatabaseError as e:
    connection.rollback()
    print(f"Error: {e}")
    print(f"Transaction rolled back: {e}")
     
finally:
     connection.close()