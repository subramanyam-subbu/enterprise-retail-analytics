/*
===========================================================
File Name   : 37_create_campaigns.sql
Module      : Marketing Management
Project     : Enterprise Retail Analytics Platform
Description : Creates the marketing campaigns table.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE campaigns (

    campaign_id INT AUTO_INCREMENT PRIMARY KEY,

    campaign_name VARCHAR(150) NOT NULL UNIQUE,

    campaign_type ENUM(
        'Seasonal',
        'Festival',
        'Flash Sale',
        'Clearance',
        'Email',
        'Social Media'
    ) NOT NULL,

    start_date DATE NOT NULL,

    end_date DATE NOT NULL,

    campaign_budget DECIMAL(12,2) NOT NULL,

    expected_revenue DECIMAL(12,2),

    campaign_status ENUM(
        'Planned',
        'Active',
        'Completed',
        'Cancelled'
    ) DEFAULT 'Planned',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);