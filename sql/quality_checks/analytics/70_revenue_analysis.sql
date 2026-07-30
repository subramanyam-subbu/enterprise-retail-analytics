-- ============================================
-- STEP 70
-- REVENUE ANALYSIS
-- ============================================

-- 1. Total Revenue from Delivered Orders

SELECT
    SUM(total_amount) AS total_revenue
FROM orders
WHERE order_status = 'Delivered';

-- 2. Total Delivered Orders

SELECT
    COUNT(*) AS delivered_orders
FROM orders
WHERE order_status = 'Delivered';

-- 3. Average Order Value

SELECT
    AVG(total_amount) AS average_order_value
FROM orders
WHERE order_status = 'Delivered';

-- 4. Revenue by Order Status

SELECT
    order_status,

    COUNT(*) AS order_count,

    SUM(total_amount) AS total_order_value,

    AVG(total_amount) AS average_order_value

FROM orders

GROUP BY order_status

ORDER BY total_order_value DESC;

-- 5. Monthly Revenue

SELECT
    YEAR(order_date) AS order_year,
    MONTH(order_date) AS order_month,

    SUM(total_amount) AS monthly_revenue,

    COUNT(*) AS delivered_orders

FROM orders

WHERE order_status = 'Delivered'

GROUP BY
    YEAR(order_date),
    MONTH(order_date)

ORDER BY
    order_year,
    order_month;

-- 6. Daily Revenue

SELECT
    DATE(order_date) AS order_date,

    COUNT(*) AS delivered_orders,

    SUM(total_amount) AS daily_revenue

FROM orders

WHERE order_status = 'Delivered'

GROUP BY DATE(order_date)

ORDER BY order_date;

-- 7. Revenue by Customer

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,

    COUNT(o.order_id) AS total_orders,

    SUM(o.total_amount) AS total_revenue

FROM customers c

INNER JOIN orders o
    ON c.customer_id = o.customer_id

WHERE o.order_status = 'Delivered'

GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name

ORDER BY total_revenue DESC;

-- 8. Top 10 Customers

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,

    COUNT(o.order_id) AS total_orders,

    SUM(o.total_amount) AS total_revenue

FROM customers c

INNER JOIN orders o
    ON c.customer_id = o.customer_id

WHERE o.order_status = 'Delivered'

GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name

ORDER BY total_revenue DESC

LIMIT 10;

-- 9. Revenue by State

SELECT
    c.state,

    COUNT(o.order_id) AS total_orders,

    SUM(o.total_amount) AS total_revenue

FROM customers c

INNER JOIN orders o
    ON c.customer_id = o.customer_id

WHERE o.order_status = 'Delivered'

GROUP BY c.state

ORDER BY total_revenue DESC;

-- 10. Revenue by City

SELECT
    c.city,

    COUNT(o.order_id) AS total_orders,

    SUM(o.total_amount) AS total_revenue

FROM customers c

INNER JOIN orders o
    ON c.customer_id = o.customer_id

WHERE o.order_status = 'Delivered'

GROUP BY c.city

ORDER BY total_revenue DESC;

-- 11. Revenue Components

SELECT

    SUM(subtotal_amount) AS total_subtotal,

    SUM(discount_amount) AS total_discount,

    SUM(tax_amount) AS total_tax,

    SUM(shipping_charges) AS total_shipping,

    SUM(total_amount) AS total_revenue

FROM orders

WHERE order_status = 'Delivered';

-- 12. Discount Analysis

SELECT

    COUNT(*) AS delivered_orders,

    SUM(discount_amount) AS total_discount,

    AVG(discount_amount) AS average_discount,

    AVG(
        discount_amount / NULLIF(subtotal_amount, 0)
    ) * 100 AS average_discount_percentage

FROM orders

WHERE order_status = 'Delivered';

-- 13. Payment Status Analysis

SELECT
    payment_status,

    COUNT(*) AS order_count,

    SUM(total_amount) AS order_value

FROM orders

GROUP BY payment_status

ORDER BY order_value DESC;

-- 14. Revenue KPI Summary

SELECT

    COUNT(*) AS delivered_orders,

    COUNT(DISTINCT customer_id)
        AS unique_customers,

    SUM(total_amount)
        AS total_revenue,

    AVG(total_amount)
        AS average_order_value,

    SUM(discount_amount)
        AS total_discount,

    SUM(tax_amount)
        AS total_tax,

    SUM(shipping_charges)
        AS total_shipping

FROM orders

WHERE order_status = 'Delivered';

