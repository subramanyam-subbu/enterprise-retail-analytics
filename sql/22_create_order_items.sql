/*
===========================================================
File Name   : 22_create_order_items.sql
Module      : Sales Management
Project     : Enterprise Retail Analytics Platform
Description : Creates the order_items transaction table.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE order_items (

    order_item_id INT AUTO_INCREMENT PRIMARY KEY,

    order_id INT NOT NULL,

    product_id INT NOT NULL,

    quantity INT NOT NULL,

    unit_price DECIMAL(10,2) NOT NULL,

    discount_amount DECIMAL(10,2) DEFAULT 0,

    tax_amount DECIMAL(10,2) DEFAULT 0,

    line_total DECIMAL(12,2) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_orderitem_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_orderitem_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);