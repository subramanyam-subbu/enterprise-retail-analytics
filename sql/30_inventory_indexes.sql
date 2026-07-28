CREATE INDEX idx_inventory_product
ON inventory(product_id);

CREATE INDEX idx_inventory_warehouse
ON inventory(warehouse_id);

CREATE INDEX idx_inventory_available
ON inventory(available_quantity);

CREATE INDEX idx_inventory_reorder
ON inventory(reorder_level);