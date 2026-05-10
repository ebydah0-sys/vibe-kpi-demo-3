# Applied Analytics Mini Project

A beginner-friendly analytics project demonstrating ETL, KPI calculations, and SQL injection protection.

## Project Structure
```
vibe-kpi-demo-3/
├── data/
│   ├── raw/
│   │   └── customers_raw.csv    # Sample customer data
│   └── db/
│       └── analytics.db         # SQLite database (created by ETL)
├── src/
│   ├── etl_load_sqlite.py       # ETL script to load CSV into SQLite
│   └── kpi_city.py              # KPI calculation with SQL injection protection
├── tests/
│   └── test_kpi_city.py         # Pytest tests for KPI functionality
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # This file
```

## Setup and Run Commands

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run ETL Script (Load CSV into SQLite)
```bash
python src/etl_load_sqlite.py
```

### 3. Run KPI Script
```bash
python src/kpi_city.py
```

### 4. Run Tests
```bash
pytest tests/test_kpi_city.py -v
```

## Features
- **ETL Pipeline**: Loads CSV data into SQLite database
- **KPI Calculations**: City-specific analytics with customer metrics
- **SQL Injection Protection**: Uses parameterized queries to prevent SQL injection
- **Unit Tests**: Pytest tests for happy path and injection protection

## Data Schema
- **customers_raw table**: customer_id (int), city (text), monthly_spend (float), churned (0/1)
- **Sample cities**: Mumbai, Delhi, Bangalore, Chennai
- **Sample rows**: 12 customers across different cities