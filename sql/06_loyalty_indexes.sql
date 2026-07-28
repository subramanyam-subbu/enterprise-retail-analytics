CREATE INDEX idx_loyalty_tier
ON loyalty_accounts(tier);

CREATE INDEX idx_loyalty_points
ON loyalty_accounts(points_balance);

CREATE INDEX idx_loyalty_status
ON loyalty_accounts(account_status);