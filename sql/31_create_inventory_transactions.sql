/*
===========================================================
File Name   : 31_create_inventory_transactions.sql
Module      : Inventory Management
Project     : Enterprise Retail Analytics Platform
Description : Tracks every inventory movement.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE inventory_transactions (

    transaction_id INT AUTO_INCREMENT PRIMARY KEY,

    inventory_id INT NOT NULL,

    transaction_type ENUM(
        'Purchase',
        'Sale',
        'Return',
        'Transfer In',
        'Transfer Out',
        'Adjustment',
        'Damaged'
    ) NOT NULL,

    quantity INT NOT NULL,

    reference_type ENUM(
        'Purchase Order',
        'Sales Order',
        'Return',
        'Manual Adjustment',
        'Warehouse Transfer'
    ) NOT NULL,

    reference_id VARCHAR(50),

    remarks VARCHAR(500),

    transaction_date DATETIME NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_inventory_transaction_inventory
        FOREIGN KEY (inventory_id)
        REFERENCES inventory(inventory_id)
        ON DELETE CASCADE
);
