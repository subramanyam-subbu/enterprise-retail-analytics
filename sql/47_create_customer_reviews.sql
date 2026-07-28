/*
===========================================================
File Name   : 47_create_customer_reviews.sql
Module      : Customer Experience
Project     : Enterprise Retail Analytics Platform
Description : Stores customer product reviews.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE customer_reviews (

    review_id INT AUTO_INCREMENT PRIMARY KEY,

    customer_id INT NOT NULL,

    product_id INT NOT NULL,

    order_id INT NOT NULL,

    rating TINYINT NOT NULL,

    review_title VARCHAR(200),

    review_text TEXT,

    is_verified_purchase BOOLEAN DEFAULT TRUE,

    review_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT chk_rating
        CHECK (rating BETWEEN 1 AND 5),

    CONSTRAINT fk_review_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_review_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    CONSTRAINT fk_review_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);