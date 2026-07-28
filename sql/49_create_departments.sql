/*
===========================================================
File Name   : 49_create_departments.sql
Module      : Organization Management
Project     : Enterprise Retail Analytics Platform
Description : Stores department master data.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE departments (

    department_id INT AUTO_INCREMENT PRIMARY KEY,

    department_name VARCHAR(100) NOT NULL UNIQUE,

    department_code VARCHAR(20) NOT NULL UNIQUE,

    manager_name VARCHAR(150),

    department_status ENUM(
        'Active',
        'Inactive'
    ) DEFAULT 'Active',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);