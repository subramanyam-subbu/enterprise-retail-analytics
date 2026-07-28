USE enterprise_retail_analytics;

CREATE TABLE brands (

    brand_id INT AUTO_INCREMENT PRIMARY KEY,

    brand_name VARCHAR(100) NOT NULL UNIQUE,

    brand_description VARCHAR(500),

    country_of_origin VARCHAR(100),

    is_active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP

);