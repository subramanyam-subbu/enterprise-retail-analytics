USE enterprise_retail_analytics;

CREATE TABLE customer_addresses (

    address_id INT AUTO_INCREMENT PRIMARY KEY,

    customer_id INT NOT NULL,

    address_type ENUM('Home','Office','Other')
        DEFAULT 'Home',

    address_line1 VARCHAR(200) NOT NULL,

    address_line2 VARCHAR(200),

    landmark VARCHAR(100),

    city VARCHAR(80) NOT NULL,

    state VARCHAR(80) NOT NULL,

    country VARCHAR(80) NOT NULL DEFAULT 'India',

    pincode VARCHAR(10) NOT NULL,

    is_default BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_customer_address
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE CASCADE
);
