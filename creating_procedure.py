# EXERCISE: Create optimized queries to manage and analyze data
# Task 1:
# Create a procedure that displays the maximum ordered quantity in the Orders Table:

import psycopg2 as connector
from psycopg2 import Error
from config import DB_CONFIG

try:
    # Establishing a connection to the database
    connection = connector.connect(**DB_CONFIG)

    cursor = connection.cursor()

    # Drop the procedure if it exists (optional)
    drop_proc_query = """DROP PROCEDURE IF EXISTS maximumorder"""
    cursor.execute(drop_proc_query)
    connection.commit()  # Commit drop procedure

    # Create the stored procedure
    max_order_proc = """
    CREATE OR REPLACE PROCEDURE maximumorder(OUT max_order INTEGER) 
    AS $$
    BEGIN
        SELECT "OrderTotal" INTO max_order FROM "Orders" ORDER BY "OrderTotal" DESC LIMIT 1;
    END;
    $$
    LANGUAGE plpgsql;
    """
    cursor.execute(max_order_proc)
    connection.commit()  # Commit create procedure

    # Call the stored procedure using CALL
    cursor.execute("CALL maximumorder()")
    
    # Fetch the result from the stored procedure
    result = cursor.fetchone()[0]  # Assuming only one row and one column returned

    print(f"The maximum order total is: {result}")

except Error as e:
    print(f"Error: {e}")
    print("Try again.")

finally:
    if connection:
        cursor.close()
        connection.close()
