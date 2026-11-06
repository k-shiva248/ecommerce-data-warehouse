# AI Prompt History – E-Commerce Data Warehouse Project

## 1. Project Overview

**Project Name:** E-Commerce Data Warehouse & ETL Pipeline

**AI Tool Used:** ChatGPT

ChatGPT was used throughout the project for understanding requirements, project planning, Python and SQL guidance, debugging, testing suggestions, and documentation.

## 2. Prompts Used

### Phase 1: Project Planning

1. Explain the complete data engineering assignment step by step.
2. Suggest a suitable dimensional data warehouse project.
3. How many steps are required to complete this project?
4. Explain the project architecture and workflow.
5. What files and folders should I create in GitHub?

### Phase 2: Sample Data Generation

1. Generate sample e-commerce datasets for customers, products, orders, and order items.
2. How can I generate realistic sample data using Python and Faker?
3. How can I generate 100,000 or more records for performance testing?
4. How can I introduce invalid records for data quality testing?

### Phase 3: Data Cleaning and Validation

1. How can I identify missing values and duplicate records?
2. How can I validate primary keys and foreign keys?
3. How can I identify invalid quantities and prices?
4. How can I separate valid and rejected records?
5. How can I save rejected records with rejection reasons?

### Phase 4: Data Transformation

1. How can I create dimension and fact tables?
2. Explain surrogate keys and foreign keys.
3. How can I create a customer dimension?
4. How can I create a product dimension?
5. How can I create a date dimension?
6. How can I create a fact sales table?
7. How can I calculate gross amount and sales amount?

### Phase 5: DuckDB and SQL

1. Explain DuckDB and how to use it in Jupyter Notebook.
2. How can I load transformed data into DuckDB?
3. How can I prevent duplicate records when rerunning the pipeline?
4. Write SQL queries for monthly revenue and top-selling products.
5. How can I calculate customer and regional sales?
6. How can I verify source and target row counts?

### Phase 6: Testing

1. Create test cases for valid records and empty input.
2. How can I test missing columns and duplicate records?
3. How can I test null values and invalid foreign keys?
4. How can I test negative quantities?
5. How can I test late-arriving records?
6. How can I verify deterministic results?
7. How can I execute tests using Pytest?

### Phase 7: Performance and Logging

1. How can I measure data generation, transformation, and loading time?
2. How can I calculate records processed per second?
3. How can I create a performance report?
4. How can I track pipeline execution status and errors?
5. How can I improve performance using vectorized Pandas operations?

### Phase 8: Documentation and GitHub

1. Create a professional README.md for the project.
2. Create a data dictionary for source and target tables.
3. What should I include in requirements.txt?
4. What should I include in .gitignore?
5. How should I organize the project files in GitHub?
6. Review the project against the assignment requirements.

