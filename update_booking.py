# Module 2 2nd exercise: Task 2
## Creating a procedure to update the booking date from bookings table under table number.


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
    RETURNS VOID AS $$
    BEGIN
        update "Bookings" set "BookingDate" = checkbooking.booking_date where "TableNumber" = checkbooking.table_number;
    END;
    $$
    LANGUAGE plpgsql;"""

    cursor.execute(check_proc_query)
    table_number = 6
    booking_date = '2024-08-06'

    cursor.execute("SELECT * FROM checkbooking(%s, %s)",(table_number, booking_date,))     # calling checkbooking function with a parameter
    # cols = [desc[0] for desc in cursor.description]
    # print(cols)
    results = cursor.fetchall()
    if results:
        print(f"Updated Successfully.")

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