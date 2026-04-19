# SQL DuckDB Basic

A simple 3-pipeline example using DuckDB for local analytics.

## What it does

1. **create-tables** — Creates `customers` and `orders` tables
2. **load-seed** — Inserts sample data
3. **transform** — Builds a `revenue_summary` table joining customers with their completed orders

## DAG

```
create-tables → load-seed → transform
```

## Run

```bash
cd sql-duckdb-basic
flowerpot validate    # check the config
flowerpot run         # execute all pipelines
```
