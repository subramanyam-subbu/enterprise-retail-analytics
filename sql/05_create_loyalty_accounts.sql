USE enterprise_retail_analytics;

CREATE TABLE loyalty_accounts (

    loyalty_id INT AUTO_INCREMENT PRIMARY KEY,

    customer_id INT NOT NULL UNIQUE,

    loyalty_number VARCHAR(30) NOT NULL UNIQUE,

    tier ENUM('Bronze','Silver','Gold','Platinum')
        DEFAULT 'Bronze',

    points_balance INT NOT NULL DEFAULT 0,

    lifetime_points INT NOT NULL DEFAULT 0,

    join_date DATE NOT NULL,

    last_activity_date DATE,

    account_status ENUM('Active','Inactive','Blocked')
        DEFAULT 'Active',

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_loyalty_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE CASCADE
);