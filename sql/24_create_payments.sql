/*
===========================================================
File Name   : 24_create_payments.sql
Module      : Sales Management
Project     : Enterprise Retail Analytics Platform
Description : Creates the payments transaction table.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE payments (

    payment_id INT AUTO_INCREMENT PRIMARY KEY,

    order_id INT NOT NULL UNIQUE,

    payment_method ENUM(
        'Credit Card',
        'Debit Card',
        'UPI',
        'Net Banking',
        'Cash on Delivery',
        'Wallet',
        'Gift Card'
    ) NOT NULL,

    payment_status ENUM(
        'Pending',
        'Success',
        'Failed',
        'Refunded'
    ) DEFAULT 'Pending',

    transaction_reference VARCHAR(100) UNIQUE,

    payment_amount DECIMAL(12,2) NOT NULL,

    payment_date DATETIME,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_payment_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE
);