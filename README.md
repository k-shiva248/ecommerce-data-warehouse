
# E-Commerce Data Warehouse & ETL Pipeline

## 1. Project Overview

This project builds a small dimensional data warehouse
for an e-commerce business using Python, Pandas, SQL
and DuckDB.

The pipeline ingests transactional CSV files, validates
records, separates rejected data, transforms valid data
into dimension and fact tables, and publishes the data
to DuckDB for analytical reporting.

## 2. Technologies Used

- Python
- Pandas
- NumPy
- DuckDB
- SQL
- Pytest
- Jupyter Notebook
- Git and GitHub

## 3. Architecture

CSV Source Data
    |
    v
Data Ingestion
    |
    v
Data Validation
    |
    +------> Rejected Records / Quarantine
    |
    v
Data Transformation
    |
    v
Dimensional Model
    |
    +------> dim_customer
    +------> dim_product
    +------> dim_date
    +------> fact_sales
    |
    v
DuckDB Warehouse
    |
    v
SQL Analytical Reports

## 4. Data Model

### Dimension Tables

- dim_customer: Customer information.
- dim_product: Product information.
- dim_date: Calendar information.

### Fact Table

- fact_sales: One row per order item belonging
  to a completed order.

### Fact Table Measures

- quantity
- unit_price
- discount
- gross_amount
- sales_amount

## 5. Data Quality Checks

The pipeline checks:

- Missing required values
- Duplicate records
- Invalid customer references
- Invalid product references
- Invalid order references
- Negative quantities
- Invalid prices
- Invalid discounts
- Invalid dates

Rejected records are separated from valid records.

## 6. Idempotency

The project includes a fact-table reload test.
Repeated loading of the same input should not increase
the number of fact records.

## 7. Performance Testing

The project includes a performance test using
100,000 synthetic order-item records.

It measures:

- Data generation time
- Transformation time
- DuckDB loading time
- Total processing time
- DataFrame memory usage

## 8. Testing

Automated tests are written using Pytest.

Run tests using:

    python -m pytest -v tests

## 9. Setup

Install the required libraries:

    pip install -r requirements.txt

Open the Jupyter Notebook:

    jupyter notebook

Run the notebook cells in sequence.

## 10. Project Outputs

- Dimensional CSV files
- DuckDB warehouse
- SQL analytical reports
- Pipeline logs
- Validation reports
- Performance report

## 11. Limitations and Future Improvements

- Add incremental loading with persistent source
  watermarks.
- Implement full slowly changing dimensions.
- Add automated scheduling.
- Add cloud storage and orchestration.
- Improve retry and recovery handling.
