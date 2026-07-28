CREATE INDEX idx_coupon_campaign
ON coupons(campaign_id);

CREATE INDEX idx_coupon_code
ON coupons(coupon_code);

CREATE INDEX idx_coupon_status
ON coupons(coupon_status);

CREATE INDEX idx_coupon_validity
ON coupons(valid_from, valid_to);