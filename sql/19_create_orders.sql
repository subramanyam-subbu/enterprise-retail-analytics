/*
===========================================================
File Name   : 19_create_orders.sql
Module      : Sales Management
Project     : Enterprise Retail Analytics Platform
Description : Creates the orders transaction table.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE orders (

    order_id INT AUTO_INCREMENT PRIMARY KEY,

    order_number VARCHAR(30) NOT NULL UNIQUE,

    customer_id INT NOT NULL,

    order_date DATETIME NOT NULL,

    order_status ENUM(
        'Pending',
        'Confirmed',
        'Packed',
        'Shipped',
        'Delivered',
        'Cancelled',
        'Returned'
    ) DEFAULT 'Pending',

    payment_status ENUM(
        'Pending',
        'Paid',
        'Refunded'
    ) DEFAULT 'Pending',

    subtotal DECIMAL(12,2) NOT NULL,

    discount_amount DECIMAL(12,2) DEFAULT 0,

    tax_amount DECIMAL(12,2) DEFAULT 0,

    shipping_charges DECIMAL(12,2) DEFAULT 0,

    total_amount DECIMAL(12,2) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_order_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);