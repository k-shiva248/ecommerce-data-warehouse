SELECT
    COUNT(*) AS total_order_items,
    SUM(quantity) AS total_quantity,
    SUM(gross_amount) AS gross_revenue,
    SUM(sales_amount) AS total_revenue
FROM fact_sales;
