/*
===========================================================
File Name   : 26_create_warehouses.sql
Module      : Inventory Management
Project     : Enterprise Retail Analytics Platform
Description : Creates the warehouse master table.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE warehouses (

    warehouse_id INT AUTO_INCREMENT PRIMARY KEY,

    warehouse_name VARCHAR(150) NOT NULL UNIQUE,

    warehouse_code VARCHAR(20) NOT NULL UNIQUE,

    city VARCHAR(100) NOT NULL,

    state VARCHAR(100) NOT NULL,

    country VARCHAR(100) NOT NULL,

    warehouse_status ENUM(
        'Active',
        'Inactive'
    ) DEFAULT 'Active',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);