/*
===========================================================
File Name   : 43_create_coupon_usage.sql
Module      : Marketing Management
Project     : Enterprise Retail Analytics Platform
Description : Tracks coupon redemption by customers.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE coupon_usage (

    usage_id INT AUTO_INCREMENT PRIMARY KEY,

    coupon_id INT NOT NULL,

    customer_id INT NOT NULL,

    order_id INT NOT NULL UNIQUE,

    discount_amount DECIMAL(10,2) NOT NULL,

    redeemed_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_coupon_usage_coupon
        FOREIGN KEY (coupon_id)
        REFERENCES coupons(coupon_id),

    CONSTRAINT fk_coupon_usage_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_coupon_usage_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE
);
