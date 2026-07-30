-- ============================================
-- STEP 69
-- CUSTOMER ORDER ANALYSIS
-- ============================================

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.city,
    c.state,

    COUNT(o.order_id) AS total_orders,

    COALESCE(
        SUM(o.total_amount),
        0
    ) AS total_spent

FROM customers c

LEFT JOIN orders o
    ON c.customer_id = o.customer_id

GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.city,
    c.state

ORDER BY total_spent DESC;

-- ============================================
-- CUSTOMERS WITH NO ORDERS
-- ============================================

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.city,
    c.state

FROM customers c

LEFT JOIN orders o
    ON c.customer_id = o.customer_id

WHERE o.order_id IS NULL;

-- ============================================
-- TOP 10 CUSTOMERS BY SPENDING
-- ============================================

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,

    COUNT(o.order_id) AS total_orders,

    COALESCE(
        SUM(o.total_amount),
        0
    ) AS total_spent

FROM customers c

LEFT JOIN orders o
    ON c.customer_id = o.customer_id

GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name

ORDER BY total_spent DESC

LIMIT 10;

-- ============================================
-- CUSTOMER AVERAGE ORDER VALUE
-- ============================================

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,

    COUNT(o.order_id) AS total_orders,

    COALESCE(
        SUM(o.total_amount),
        0
    ) AS total_spent,

    COALESCE(
        AVG(o.total_amount),
        0
    ) AS average_order_value

FROM customers c

LEFT JOIN orders o
    ON c.customer_id = o.customer_id

GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name

ORDER BY total_spent DESC;

-- ============================================
-- ORDER STATUS DISTRIBUTION
-- ============================================

SELECT
    order_status,
    COUNT(*) AS order_count,

    SUM(total_amount) AS order_value

FROM orders

GROUP BY order_status

ORDER BY order_count DESC;