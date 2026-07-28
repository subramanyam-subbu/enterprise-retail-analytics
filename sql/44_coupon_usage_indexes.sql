CREATE INDEX idx_coupon_usage_coupon
ON coupon_usage(coupon_id);

CREATE INDEX idx_coupon_usage_customer
ON coupon_usage(customer_id);

CREATE INDEX idx_coupon_usage_order
ON coupon_usage(order_id);

CREATE INDEX idx_coupon_usage_redeemed
ON coupon_usage(redeemed_at);