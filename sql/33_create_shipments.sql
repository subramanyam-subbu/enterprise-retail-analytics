/*
===========================================================
File Name   : 33_create_shipments.sql
Module      : Shipping Management
Project     : Enterprise Retail Analytics Platform
Description : Stores shipment details for customer orders.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE shipments (

    shipment_id INT AUTO_INCREMENT PRIMARY KEY,

    order_id INT NOT NULL UNIQUE,

    courier_name VARCHAR(100) NOT NULL,

    tracking_number VARCHAR(100) NOT NULL UNIQUE,

    shipment_status ENUM(
        'Pending',
        'Packed',
        'Shipped',
        'In Transit',
        'Out For Delivery',
        'Delivered',
        'Failed',
        'Returned'
    ) DEFAULT 'Pending',

    shipping_cost DECIMAL(10,2) DEFAULT 0.00,

    shipped_date DATETIME,

    expected_delivery_date DATETIME,

    actual_delivery_date DATETIME,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_shipment_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE
);