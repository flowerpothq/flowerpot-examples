# SQL DuckDB Basic

A simple 3-pipeline example using the DuckDB CLI for local analytics.

## Prerequisites

Install DuckDB: `brew install duckdb` (or see [duckdb.org/docs/installation](https://duckdb.org/docs/installation))

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

# verify results
duckdb data/analytics.duckdb "SELECT * FROM revenue_summary"
```
