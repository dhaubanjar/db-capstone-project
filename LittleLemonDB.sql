-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://github.com/pgadmin-org/pgadmin4/issues/new/choose if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public."Orders"
(
    "OrderID" integer NOT NULL,
    "OrderTotal" numeric NOT NULL,
    "CustomerID" integer NOT NULL,
    "StaffID" integer NOT NULL,
    "MenuID" integer NOT NULL,
    PRIMARY KEY ("OrderID")
);

CREATE TABLE IF NOT EXISTS public."Customers"
(
    "CustomerID" integer NOT NULL,
    "Name" character varying(255) NOT NULL,
    "ContactNumber" character varying(50) NOT NULL,
    "Email" character varying(50) NOT NULL,
    PRIMARY KEY ("CustomerID")
);

CREATE TABLE IF NOT EXISTS public."Staffs"
(
    "StaffID" integer NOT NULL,
    "StaffName" character varying(100) NOT NULL,
    "Role" character varying(50) NOT NULL,
    "Username" character varying(50) NOT NULL,
    "Password" character varying(50) NOT NULL,
    "BookingID" integer NOT NULL,
    "DeliveryID" integer NOT NULL,
    PRIMARY KEY ("StaffID")
);

CREATE TABLE IF NOT EXISTS public."Menu"
(
    "MenuID" integer NOT NULL,
    "Name" character varying(100) NOT NULL,
    "Category" character varying(100) NOT NULL,
    "Price" numeric(50) NOT NULL,
    "MenuCategoryID" integer NOT NULL,
    PRIMARY KEY ("MenuID")
);

CREATE TABLE IF NOT EXISTS public."Bookings"
(
    "BookingID" integer NOT NULL,
    "Bill" numeric(50) NOT NULL,
    "TableNumber" integer NOT NULL,
    "Discount" numeric(50),
    "Tax" numeric(50),
    "CustomerID" integer NOT NULL,
    "MenuID" integer NOT NULL,
    "DeliveryID" integer NOT NULL,
    PRIMARY KEY ("BookingID")
);

CREATE TABLE IF NOT EXISTS public."Delivery"
(
    "DeliveryID" integer NOT NULL,
    "DeliveryStatus" character varying(10) NOT NULL,
    "Comment" character varying(255),
    "AddressID" integer NOT NULL,
    PRIMARY KEY ("DeliveryID")
);

CREATE TABLE IF NOT EXISTS public."Address"
(
    "AddressID" integer NOT NULL,
    "Address" character varying(255) NOT NULL,
    "City" character varying(100) NOT NULL,
    "State" character varying(100) NOT NULL,
    "Country" character varying(100) NOT NULL,
    zipcode integer NOT NULL,
    PRIMARY KEY ("AddressID")
);

CREATE TABLE IF NOT EXISTS public."MenuCategory"
(
    "MenuCategoryID" integer NOT NULL,
    "Type" character varying(100) NOT NULL,
    "Description" character varying(255) NOT NULL,
    "MenuSubCategoryID" integer NOT NULL,
    "MenuItemID" integer NOT NULL,
    PRIMARY KEY ("MenuCategoryID")
);

CREATE TABLE IF NOT EXISTS public."MenuSubCategory"
(
    "MenuSubCategoryID" integer NOT NULL,
    "Type" character varying(100) NOT NULL,
    PRIMARY KEY ("MenuSubCategoryID")
);

CREATE TABLE IF NOT EXISTS public."MenuItems"
(
    "MenuItemID" integer NOT NULL,
    "ItemName" character varying(100) NOT NULL,
    "Price" numeric(50) NOT NULL,
    "Description" character varying(255) NOT NULL,
    PRIMARY KEY ("MenuItemID")
);

ALTER TABLE IF EXISTS public."Orders"
    ADD CONSTRAINT "Orders_StaffID_FK" FOREIGN KEY ("StaffID")
    REFERENCES public."Staffs" ("StaffID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Orders"
    ADD CONSTRAINT "Orders_MenuID_FK" FOREIGN KEY ("MenuID")
    REFERENCES public."Menu" ("MenuID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Orders"
    ADD CONSTRAINT "Orders_CustomerID_FK" FOREIGN KEY ("CustomerID")
    REFERENCES public."Customers" ("CustomerID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Staffs"
    ADD CONSTRAINT "Staffs_DeliveryID_FK" FOREIGN KEY ("DeliveryID")
    REFERENCES public."Delivery" ("DeliveryID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Staffs"
    ADD CONSTRAINT "Staffs_BookingID_FK" FOREIGN KEY ("BookingID")
    REFERENCES public."Bookings" ("BookingID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Menu"
    ADD CONSTRAINT "Menu_MenuCategoryID_FK" FOREIGN KEY ("MenuCategoryID")
    REFERENCES public."MenuCategory" ("MenuCategoryID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Bookings"
    ADD CONSTRAINT "Bookings_CustomerID_FK" FOREIGN KEY ("CustomerID")
    REFERENCES public."Customers" ("CustomerID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Bookings"
    ADD CONSTRAINT "Bookings_MenuID_FK" FOREIGN KEY ("MenuID")
    REFERENCES public."Menu" ("MenuID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Delivery"
    ADD CONSTRAINT "Delivery_AddressID_FK" FOREIGN KEY ("AddressID")
    REFERENCES public."Address" ("AddressID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."MenuCategory"
    ADD CONSTRAINT "MenuCategory_MenuSubCategoryID_FK" FOREIGN KEY ("MenuSubCategoryID")
    REFERENCES public."MenuSubCategory" ("MenuSubCategoryID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."MenuCategory"
    ADD CONSTRAINT "MenuCategory_MenuItemID_FK" FOREIGN KEY ("MenuItemID")
    REFERENCES public."MenuItems" ("MenuItemID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;