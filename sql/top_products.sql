SELECT
    p.product_name,
    SUM(f.quantity) AS units_sold,
    SUM(f.sales_amount) AS total_revenue
FROM fact_sales f
JOIN dim_product p
    ON f.product_key = p.product_key
GROUP BY p.product_name
ORDER BY total_revenue DESC
LIMIT 5;
