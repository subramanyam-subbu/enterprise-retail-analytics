CREATE INDEX idx_brand_name
ON brands(brand_name);

CREATE INDEX idx_brand_active
ON brands(is_active);

CREATE INDEX idx_brand_country
ON brands(country_of_origin);