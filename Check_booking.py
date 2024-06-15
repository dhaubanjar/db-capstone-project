import psycopg2 as connector
from psycopg2 import Error
from config import DB_CONFIG

try:
    connection = connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    # Drop the procedure if it exists (optional)
    drop_proc_query = """DROP FUNCTION IF EXISTS checkbooking() CASCADE"""
    cursor.execute(drop_proc_query)
    connection.commit()  # Commit drop procedure

    check_proc_query = """CREATE OR REPLACE FUNCTION checkbooking()
    RETURNS TABLE(BookingID INTEGER,
    Bill Numeric,
    TableNumber INTEGER,
    Discount NUMERIC,
    Tax NUMERIC,
    CustomerID INTEGER,
    MenuID INTEGER,
    DeliveryID INTEGER) AS $$
    BEGIN
        RETURN QUERY SELECT * FROM "Bookings";
    END;
    $$
    LANGUAGE plpgsql;"""

    cursor.execute(check_proc_query)
    connection.commit()

    cursor.execute("SELECT checkbooking();")
    results = cursor.fetchall()
    for i in results:
        print(i)

except Error as e:
    print(f"Error: {e}")
    print("Try again.")
     
finally:
     connection.close()