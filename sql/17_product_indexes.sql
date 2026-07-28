CREATE INDEX idx_product_name
ON products(product_name);

CREATE INDEX idx_product_category
ON products(category_id);

CREATE INDEX idx_product_brand
ON products(brand_id);

CREATE INDEX idx_product_supplier
ON products(supplier_id);

CREATE INDEX idx_product_status
ON products(product_status);

CREATE INDEX idx_product_price
ON products(unit_price);