CREATE INDEX idx_orderitem_order
ON order_items(order_id);

CREATE INDEX idx_orderitem_product
ON order_items(product_id);

CREATE INDEX idx_orderitem_quantity
ON order_items(quantity);

CREATE INDEX idx_orderitem_total
ON order_items(line_total);
