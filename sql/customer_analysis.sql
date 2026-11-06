SELECT
    c.customer_name,
    COUNT(DISTINCT f.order_id) AS total_orders,
    SUM(f.sales_amount) AS total_spent
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_key = c.customer_key
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 10;
