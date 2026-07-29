USE enterprise_retail_analytics;

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,

    department_id INT NOT NULL,

    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,

    email VARCHAR(150) NOT NULL UNIQUE,
    phone_number VARCHAR(20) UNIQUE,

    designation VARCHAR(100) NOT NULL,

    hire_date DATE NOT NULL,

    salary DECIMAL(12,2) NOT NULL,

    manager_id INT NULL,

    employment_status ENUM('Active','Inactive','Resigned')
        DEFAULT 'Active',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id),

    CONSTRAINT fk_employee_manager
        FOREIGN KEY (manager_id)
        REFERENCES employees(employee_id)
);