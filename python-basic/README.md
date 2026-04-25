# Python Basic

A 3-pipeline ETL example using Python scripts with `uv`-managed dependencies.

## Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/) — `brew install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`

`uv` is used to install inline dependencies (the `transform` step uses `tabulate`). No virtualenv setup is needed — `uv run --with` handles it automatically.

## What it does

1. **extract** — Generates sample user records as JSON
2. **transform** — Reads raw data, applies grading logic, prints a formatted table (via `tabulate`)
3. **load** — Reads transformed data, prints a summary report

## DAG

```
extract → transform → load
```

## Run

```bash
cd python-basic
flowerpot validate
flowerpot run
```
