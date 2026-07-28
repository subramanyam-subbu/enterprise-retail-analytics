CREATE INDEX idx_payment_status
ON payments(payment_status);

CREATE INDEX idx_payment_method
ON payments(payment_method);

CREATE INDEX idx_payment_date
ON payments(payment_date);

CREATE INDEX idx_payment_amount
ON payments(payment_amount);