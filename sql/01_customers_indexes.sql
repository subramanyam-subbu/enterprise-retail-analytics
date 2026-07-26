CREATE INDEX idx_customer_city
ON customers(city);

CREATE INDEX idx_customer_state
ON customers(state);

CREATE INDEX idx_customer_registration
ON customers(registration_date);

CREATE INDEX idx_customer_status
ON customers(customer_status);

CREATE INDEX idx_customer_loyalty
ON customers(loyalty_tier);