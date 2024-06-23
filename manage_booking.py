# Module 2: Task 3
## Creating a procedure to check the booking id if it exists or not in the table.
# In postgresql, there is no stored procedure, instead it have a function, so creaing a function.
# In this code, In the else statement, I didn't add the code which insert the values in the Bookings table because the foreign key constraints that i created
# won't let adding the new data before adding the customer ID = 6 in the customers table.

import psycopg2 
from psycopg2 import Error
from config import DB_CONFIG

try:
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()

    #Begin the TRANSACTION
    cursor.execute("BEGIN;")

    # Drop the procedure if it exists (optional)
    drop_proc_query = """DROP FUNCTION IF EXISTS AddValidBooking(booking_date DATE, table_number Integer) CASCADE"""
    cursor.execute(drop_proc_query)
    connection.commit()  # Commit drop procedure


    #creating a function AddValidBooking which accepts a parameter
    check_proc_query = """CREATE OR REPLACE FUNCTION AddValidBooking(booking_date Date, table_number INTEGER)      
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
        RETURN QUERY SELECT * FROM "Bookings" WHERE "BookingDate" = AddValidBooking.booking_date AND "TableNumber" = AddValidBooking.table_number;
    END;
    $$
    LANGUAGE plpgsql;"""

    cursor.execute(check_proc_query)
    table_number = 3
    booking_date = '2024-06-06'

    cursor.execute("SELECT * FROM AddValidBooking(%s , %s)",(booking_date, table_number, ))     # calling AddValidBooking function with a parameter
    # cols = [desc[0] for desc in cursor.description]
    # print(cols)
    results = cursor.fetchall()
    if results:
        print("Already Booked")
        for i in results:
            print(i)
    else:
        print("The booking must be added.")

except psycopg2.DatabaseError as e:
    connection.rollback()
    print(f"Error: {e}")
    print(f"Transaction rolled back: {e}")
     
finally:
     connection.close()