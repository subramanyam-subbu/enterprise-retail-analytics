/*
===========================================================
File Name   : 45_create_returns.sql
Module      : Returns Management
Project     : Enterprise Retail Analytics Platform
Description : Stores customer return requests.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE returns (

    return_id INT AUTO_INCREMENT PRIMARY KEY,

    order_item_id INT NOT NULL,

    customer_id INT NOT NULL,

    return_reason ENUM(
        'Damaged',
        'Wrong Item',
        'Defective',
        'Changed Mind',
        'Size Issue',
        'Late Delivery',
        'Other'
    ) NOT NULL,

    return_status ENUM(
        'Requested',
        'Approved',
        'Rejected',
        'Refunded'
    ) DEFAULT 'Requested',

    refund_amount DECIMAL(10,2) NOT NULL,

    return_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    remarks VARCHAR(500),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_return_order_item
        FOREIGN KEY (order_item_id)
        REFERENCES order_items(order_item_id),

    CONSTRAINT fk_return_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);