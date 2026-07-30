SELECT
    COUNT(*) AS total_products
FROM products;

SELECT
    COUNT(*) AS missing_product_names
FROM products
WHERE product_name IS NULL
   OR TRIM(product_name) = '';

SELECT
    COUNT(*) AS invalid_prices
FROM products
WHERE unit_price <= 0
   OR cost_price <= 0;

SELECT
    COUNT(*) AS invalid_cost_products
FROM products
WHERE cost_price > unit_price;

SELECT
    COUNT(*) AS invalid_stock
FROM products
WHERE stock_quantity < 0
   OR reorder_level < 0;

SELECT
    product_status,
    COUNT(*) AS product_count
FROM products
GROUP BY product_status
ORDER BY product_count DESC;

SELECT
    category_id,
    COUNT(*) AS product_count
FROM products
GROUP BY category_id
ORDER BY product_count DESC;

SELECT
    supplier_id,
    COUNT(*) AS product_count
FROM products
GROUP BY supplier_id
ORDER BY product_count DESC;

