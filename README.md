
# E-Commerce Data Warehouse & ETL Pipeline

## 1. Project Overview

This project implements a small dimensional data warehouse for an e-commerce business using Python, Pandas, SQL and DuckDB.

The solution processes transactional CSV data, validates records, handles data-quality issues, transforms valid records into dimension and fact tables, and publishes the results into a DuckDB analytical warehouse.

The objective is to demonstrate an end-to-end data engineering workflow covering data ingestion, validation, transformation, dimensional modeling, data publishing, testing, performance measurement and documentation.

## 2. Business Problem

E-commerce businesses generate transactional data from customers, products, orders and order items.

Analyzing this data directly from transactional sources can make reporting difficult because information is distributed across multiple files and requires cleaning and transformation.

This project addresses the problem by building a centralized dimensional model that supports analytical questions such as:

- What is the total sales revenue?
- What is the monthly revenue?
- Which products generate the highest revenue?
- Which customers contribute the most sales?
- How does revenue vary across product categories and regions?

## 3. Project Objectives

- Build a dimensional data warehouse from transactional sources.
- Define source and target schemas.
- Implement data ingestion and validation.
- Identify and quarantine invalid records.
- Create dimension and fact tables.
- Maintain primary-key and foreign-key relationships.
- Implement safe fact-table reload behavior.
- Generate analytical reports using SQL.
- Test important data-quality scenarios.
- Measure performance using 100,000 synthetic records.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Pipeline implementation |
| Pandas | Data cleaning and transformation |
| NumPy | Numerical operations and data generation |
| Faker | Synthetic data generation |
| DuckDB | Analytical database |
| SQL | Analytical queries |
| Pytest | Automated testing |
| Jupyter Notebook | Development and execution |
| GitHub | Version control and project submission |

## 5. Project Architecture

The pipeline follows this architecture:

```mermaid
flowchart TD
    A[Transactional CSV Sources] --> B[Data Ingestion]
    B --> C[Schema Validation]
    C --> D[Business Rule Validation]
    D --> E[Valid Records]
    D --> F[Rejected Records / Quarantine]
    E --> G[Data
