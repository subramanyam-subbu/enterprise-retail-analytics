/*
===========================================================
File Name   : 29_create_inventory.sql
Module      : Inventory Management
Project     : Enterprise Retail Analytics Platform
Description : Stores inventory by warehouse.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE inventory (

    inventory_id INT AUTO_INCREMENT PRIMARY KEY,

    warehouse_id INT NOT NULL,

    product_id INT NOT NULL,

    available_quantity INT NOT NULL DEFAULT 0,

    reserved_quantity INT NOT NULL DEFAULT 0,

    damaged_quantity INT NOT NULL DEFAULT 0,

    reorder_level INT NOT NULL DEFAULT 20,

    last_stock_update DATETIME DEFAULT CURRENT_TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_inventory_warehouse
        FOREIGN KEY (warehouse_id)
        REFERENCES warehouses(warehouse_id),

    CONSTRAINT fk_inventory_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    CONSTRAINT uq_inventory
        UNIQUE (warehouse_id, product_id)
);