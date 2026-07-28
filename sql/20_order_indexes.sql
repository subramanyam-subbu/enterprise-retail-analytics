CREATE INDEX idx_orders_customer
ON orders(customer_id);

CREATE INDEX idx_orders_date
ON orders(order_date);

CREATE INDEX idx_orders_status
ON orders(order_status);

CREATE INDEX idx_orders_payment
ON orders(payment_status);

CREATE INDEX idx_orders_total
ON orders(total_amount);