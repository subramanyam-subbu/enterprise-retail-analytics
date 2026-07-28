/*
===========================================================
File Name   : 16_create_products.sql
Module      : Product Management
Project     : Enterprise Retail Analytics Platform
Description : Creates the products master table.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE products (

    product_id INT AUTO_INCREMENT PRIMARY KEY,

    product_name VARCHAR(200) NOT NULL,

    product_sku VARCHAR(50) NOT NULL UNIQUE,

    category_id INT NOT NULL,

    brand_id INT NOT NULL,

    supplier_id INT NOT NULL,

    unit_price DECIMAL(10,2) NOT NULL,

    cost_price DECIMAL(10,2) NOT NULL,

    stock_quantity INT NOT NULL DEFAULT 0,

    reorder_level INT NOT NULL DEFAULT 10,

    product_status ENUM('Active','Inactive','Discontinued')
        DEFAULT 'Active',

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_product_category
        FOREIGN KEY (category_id)
        REFERENCES categories(category_id),

    CONSTRAINT fk_product_brand
        FOREIGN KEY (brand_id)
        REFERENCES brands(brand_id),

    CONSTRAINT fk_product_supplier
        FOREIGN KEY (supplier_id)
        REFERENCES suppliers(supplier_id)
);