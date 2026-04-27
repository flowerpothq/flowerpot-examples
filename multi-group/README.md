# Multi-Group Pipeline Example

Demonstrates **pipeline groups** -- composing multiple sub-config files into a single DAG with cross-group dependencies.

## What this shows

- **Multi-file config**: A root `flowerpot.yaml` composes three sub-configs
- **Three execution modes** in one project: Python scripts, SQL (DuckDB), and Docker
- **Cross-group dependencies**: analytics waits for ingestion, scoring waits for analytics
- **Auto-prefixed pipeline names**: `ingestion.extract`, `analytics.aggregate`, etc.
- **Group metadata**: each group carries a human-readable name and tags

## DAG

```
ingestion.extract ──► ingestion.normalize ──┐
                                            ├──► analytics.aggregate ──┐
            analytics.create_tables ────────┘                          │
                                                                       ├──► scoring.score
                                         scoring.build ────────────────┘
```

7 pipelines across 3 groups:

| Group       | Pipelines                               | Mode   |
|-------------|-----------------------------------------|--------|
| ingestion   | extract, normalize                      | Python |
| analytics   | create_tables, aggregate                | SQL    |
| scoring     | build, score                            | Docker |

## Prerequisites

- Python 3.10+
- [DuckDB CLI](https://duckdb.org/docs/installation/) (for SQL pipelines)
- Docker (for scoring pipelines)
- Flowerpot CLI

## Running

```bash
flowerpot validate  # Validate the config
flowerpot run       # Run the full DAG
flowerpot ui        # View in the TUI
```

## Expected execution order

1. `ingestion.extract` and `analytics.create_tables` and `scoring.build` (no deps, run in parallel)
2. `ingestion.normalize` (after extract)
3. `analytics.aggregate` (after create_tables + ingestion.normalize)
4. `scoring.score` (after scoring.build + analytics.aggregate)
