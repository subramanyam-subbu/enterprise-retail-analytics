USE enterprise_retail_analytics;

CREATE TABLE suppliers (

    supplier_id INT AUTO_INCREMENT PRIMARY KEY,

    supplier_name VARCHAR(150) NOT NULL UNIQUE,

    contact_person VARCHAR(120) NOT NULL,

    email VARCHAR(150) NOT NULL UNIQUE,

    phone VARCHAR(20) NOT NULL UNIQUE,

    country VARCHAR(100) NOT NULL,

    state VARCHAR(100) NOT NULL,

    city VARCHAR(100) NOT NULL,

    gst_number VARCHAR(30) UNIQUE,

    payment_terms ENUM(
        'Advance',
        '15 Days',
        '30 Days',
        '45 Days',
        '60 Days'
    ) DEFAULT '30 Days',

    supplier_status ENUM(
        'Active',
        'Inactive',
        'Blocked'
    ) DEFAULT 'Active',

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP

);