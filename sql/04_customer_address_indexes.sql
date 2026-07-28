CREATE INDEX idx_customer_address_customer
ON customer_addresses(customer_id);

CREATE INDEX idx_customer_address_city
ON customer_addresses(city);

CREATE INDEX idx_customer_address_state
ON customer_addresses(state);

CREATE INDEX idx_customer_address_default
ON customer_addresses(is_default);