CREATE INDEX idx_return_customer
ON returns(customer_id);

CREATE INDEX idx_return_status
ON returns(return_status);

CREATE INDEX idx_return_reason
ON returns(return_reason);

CREATE INDEX idx_return_date
ON returns(return_date);