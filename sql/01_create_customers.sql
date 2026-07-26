USE enterprise_retail_analytics;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,

    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,

    gender ENUM('Male','Female','Other') NOT NULL,

    date_of_birth DATE,

    email VARCHAR(150) NOT NULL UNIQUE,

    phone_number VARCHAR(20) NOT NULL UNIQUE,

    registration_date DATETIME NOT NULL,

    customer_status ENUM('Active','Inactive','Blocked')
        DEFAULT 'Active',

    loyalty_tier ENUM('Bronze','Silver','Gold','Platinum')
        DEFAULT 'Bronze',

    preferred_language VARCHAR(30)
        DEFAULT 'English',

    preferred_contact ENUM('Email','SMS','Phone')
        DEFAULT 'Email',

    city VARCHAR(80) NOT NULL,
    state VARCHAR(80) NOT NULL,
    country VARCHAR(80) NOT NULL,
    pincode VARCHAR(15) NOT NULL,

    marketing_consent BOOLEAN
        DEFAULT TRUE,

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);