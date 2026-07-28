/*
===========================================================
File Name   : 40_create_coupons.sql
Module      : Marketing Management
Project     : Enterprise Retail Analytics Platform
Description : Creates coupons master table.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE coupons (

    coupon_id INT AUTO_INCREMENT PRIMARY KEY,

    campaign_id INT NOT NULL,

    coupon_code VARCHAR(50) NOT NULL UNIQUE,

    discount_type ENUM(
        'Percentage',
        'Flat Amount',
        'Free Shipping'
    ) NOT NULL,

    discount_value DECIMAL(10,2) NOT NULL,

    minimum_order_amount DECIMAL(10,2) DEFAULT 0,

    maximum_discount DECIMAL(10,2),

    valid_from DATE NOT NULL,

    valid_to DATE NOT NULL,

    usage_limit INT DEFAULT 1000,

    coupon_status ENUM(
        'Active',
        'Inactive',
        'Expired'
    ) DEFAULT 'Active',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_coupon_campaign
        FOREIGN KEY (campaign_id)
        REFERENCES campaigns(campaign_id)
);