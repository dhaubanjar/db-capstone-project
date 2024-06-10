import psycopg2 as connector
from psycopg2 import Error, sql
from faker import Faker
import numpy as np
import pandas as pd
import random

#instantiating faker class
fake = Faker()
#--------------------Function for Customers
def makeCustomer(num):
    CustomerID = []
    Name =[]
    ContactNumber = []
    Email = []

    for i in range(num):
        CustomerID.append(i+1)

    for _ in range(num):
        Name.append(fake.name())

    for _ in range(num):
        ContactNumber.append(fake.phone_number())

    for _ in range(num):
        Email.append(fake.email())

    data = list(zip(CustomerID, Name, ContactNumber, Email))
    return data

#--------------------Function for MENUITEMS
def makeMenuItem(num):
    MenuItemID = []
    ItemName = []
    Price = []
    Description = []

    for i in range(num):
        MenuItemID.append(i+1)

    for _ in range(num):
        ItemName.append(fake.name())

    for _ in range(num):
        
        Price.append(round(fake.random_number(digits=5, fix_len=False) / 100, 2))

    for _ in range(num):
        Description.append(fake.sentences())
    
    data = list(zip(MenuItemID, ItemName, Price, Description))
    return(data)

#--------------------Function for SUBCATEGORY
def makeSubcategory(num):
    MenuSubCategoryID = []
    Type = []
    MenuItemID = []

    for i in range(num):
        MenuSubCategoryID.append(i+1)

    for i in range(num):
        Type.append(fake.name())

    
    data = list(zip(MenuSubCategoryID, Type))
    return(data)

#--------------------Function for CATEGORY
def makeMenuCategory(num):
    MenuCategoryID = []
    Type = []
    Description =[]
    MenuSubCategoryID = []

    for i in range(num):
        MenuCategoryID.append(i+1)
    
    for _ in range(num):
        Type.append(fake.name())

    for _ in range(num):
        Description.append(fake.name_nonbinary())
    
    for _ in range(num):
        MenuSubCategoryID.append(i + 1)
    data = list(zip(MenuCategoryID, Type, Description, MenuSubCategoryID))
    return(data)

#--------------------Function for MENU
def makeMenu(num):
    MenuID = []
    Name = []
    Category = []
    Price = []
    MenuCategoryID = []

    for i in range(num):
        MenuID.append(i + 1)

    for _ in range(num):
        Name.append(fake.name())

    for _ in range(num):
        Category.append(fake.name_female())
    
    for _ in range(num):
        Price.append(round(fake.random_number(digits=5, fix_len=False) / 100, 2))

    for i in range(num):
        MenuCategoryID.append(i + 1)

    data = list(zip(MenuID, Name, Category, Price, MenuCategoryID))
    return(data)

#--------------------Function for Bookings
def makeBooking(num):
    BookingID = []
    Bill = []
    TableNumber = []
    Discount = []
    Tax = []
    CustomerID = []
    MenuID = []
    DeliveryID = []

    for i in range(num):
        BookingID.append(i + 1)
    
    for _ in range(num):
         Bill.append(round(fake.random_number(digits=5, fix_len=False) / 100, 2))

    for _ in range(num):
        TableNumber.append(random.randint(1,15))
    
    for _ in range(num):
        Discount.append(random.randint(1,10))

    for _ in range(num):
        Tax.append(random.randint(1,10))

    for i in range(num):
        CustomerID.append(i + 1)

    for i in range(num):
        MenuID.append(i + 1)

    for i in range(num):
        DeliveryID.append(i + 1)

    data = list(zip(BookingID, Bill, TableNumber, Discount, Tax, CustomerID, MenuID, DeliveryID))
    return(data)

#--------------------Function for ADDRESS
def makeAddress(num):
    AddressID = []
    Address = []
    City = []
    State = []
    Country = []
    zipcode = []

    for i in range(num):
        AddressID.append(i +1)
    for _ in range(num):
        Address.append(fake.address())
    for _ in range(num):
        City.append(fake.city())
    for _ in range(num):
        State.append(fake.state())
    for _ in range(num):
        Country.append(fake.country())
    for _ in range(num):
        zipcode.append(fake.zipcode_in_state())
    data = list(zip(AddressID, Address, City, State, Country, zipcode))
    return(data)

#--------------------Function for Delivery
def makeDelivery(num):
    DeliveryID = []
    DeliveryStatus = []
    Comment = []
    AddressID = []

    for i in range(num):
        DeliveryID.append(i + 1)

    for _ in range(num):
        DeliveryStatus.append(fake.word())
    
    for _ in range(num):
        Comment.append(fake.sentences())

    for i in range(num):
        AddressID.append(i + 1)

    data = list(zip(DeliveryID, DeliveryStatus, Comment, AddressID))
    return(data)

#--------------------Function for Staff
def makeStaff(num):
    StaffID = []
    StaffName = []
    Role = []
    Username = []
    Password = []
    BookingID = []
    DeliveryID = []
    roles = ['Admin', 'User', 'Guest', 'Manager', 'Staff']
    for i in range(num):
        StaffID.append(i+1)
    
    for _ in range(num):
        StaffName.append(fake.name())
    
    for _ in range(num):
        Role.append(fake.random_choices(roles))

    for _ in range(num):
        Username.append(fake.user_name())

    for _ in range(num):
        Password.append(fake.password())
    
    for _ in range(num):
        BookingID.append(i+1)

    for _ in range(num):
        DeliveryID.append(i + 1)

    data = list(zip(StaffID, StaffName, Role, Username, Password, BookingID, DeliveryID))
    return(data)

#--------------------Function for Orders
def makeOrder(num):
    OrderID =[]
    OrderTotal =[]
    CustomerID =[]
    StaffID =[]
    MenuID =[]

    for i in range(num):
        OrderID.append(i +1)

    for _ in range(num):
        OrderTotal.append(np.random.randint(300,1000))

    for i in range(num):
        CustomerID.append(i +1 )

    for i in range(num):
        StaffID.append(i +1)

    for i in range(num):
        MenuID.append(i +1)

    data = list(zip(OrderID, OrderTotal, CustomerID, StaffID, MenuID))
    return data

#FUNCTIONS CALLS

# customer_data = makeCustomer(5)
# menuitem_data = makeMenuItem(5)
# subcategory_data = makeSubcategory(5)
# menucategory_data = makeMenuCategory(5)
# menu_data = makeMenu(5)
# address_data = makeAddress(5)
# delivery_data = makeDelivery(5)
# booking_data = makeBooking(5)
# staff_data = makeStaff(5)
order_data = makeOrder(5)
#connecting to the database
try:
    connection = connector.connect(host = "localhost", user="postgres", password="Bhaktapur@2024", dbname="LittleLemonDB")
    cursor = connection.cursor()

                    #------------QUERY TO INSERT INTO CUSTOMERS TABLE
    # insert_customers = """Insert into "Customers" ("CustomerID", "Name", "ContactNumber", "Email")
    # VALUES
    # (%s, %s, %s, %s);"""
    # cursor.executemany(insert_customers, customer_data)

                    #-------------QUERY TO INSERT MENUITEMS
    # insert_customers = """Insert into "MenuItems" ("MenuItemID", "ItemName", "Price", "Description")
    # VALUES
    # (%s, %s, %s, %s);"""
    # cursor.executemany(insert_customers, menuitem_data)

                    #-------------QUERY TO INSERT SUBCATEGORY
    # insert_subcategory = """Insert into "MenuSubCategory" ("MenuSubCategoryID", "Type")
    # VALUES
    # (%s, %s);"""
    # cursor.executemany(insert_subcategory, subcategory_data)

    #                 # -------------QUERY TO INSERT CATEGORY
    # insert_category = """Insert into "MenuCategory" ("MenuCategoryID", "Type", "Description", "MenuSubCategoryID")
    # VALUES
    # (%s, %s, %s, %s);"""
    # cursor.executemany(insert_category, menucategory_data)

    #                 # -------------QUERY TO INSERT Menu
    # insert_menu = """Insert into "Menu" ("MenuID", "Name", "Category", "Price", "MenuCategoryID")
    # VALUES
    # (%s, %s, %s, %s, %s);"""
    # cursor.executemany(insert_menu, menu_data)

                  # -------------QUERY TO INSERT Address
    # insert_address = """Insert into "Address" ("AddressID", "Address", "City", "State", "Country", "zipcode")
    # VALUES
    # (%s, %s, %s, %s, %s, %s);"""
    # cursor.executemany(insert_address, address_data)

    #               # -------------QUERY TO INSERT Delivery
    # insert_delivery = """Insert into "Delivery" ("DeliveryID", "DeliveryStatus", "Comment", "AddressID")
    # VALUES
    # (%s, %s, %s, %s);"""
    # cursor.executemany(insert_delivery, delivery_data)

                  # -------------QUERY TO INSERT Bookings
    # insert_booking = """Insert into "Bookings" ("BookingID", "Bill", "TableNumber", "Discount", "Tax", "CustomerID", "MenuID", "DeliveryID")
    # VALUES 
    # (%s, %s, %s, %s, %s, %s, %s, %s);"""
    # cursor.executemany(insert_booking, booking_data)

                  # -------------QUERY TO INSERT Staff
    # insert_staff = """Insert into "Staffs" ("StaffID", "StaffName", "Role", "Username", "Password", "BookingID", "DeliveryID")
    # VALUES
    # (%s, %s, %s, %s, %s, %s, %s );"""
    # cursor.executemany(insert_staff, staff_data)

                    # -------------QUERY TO INSERT ORDERS
    use_database_query ="""Insert into "Orders" ("OrderID", "OrderTotal", "CustomerID", "StaffID", "MenuID" ) 
    VALUES 
    (%s, %s, %s, %s, %s);"""
    cursor.executemany(use_database_query, order_data)

    connection.commit()
    print("Data inserted successfully")

except Error as e:
    print(f"Error: {e}")
    print("Try again.")
    

