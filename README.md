# Flowerpot Examples

Real-world example projects that use Flowerpot. Each directory is a standalone project you can clone and run.

## Examples

| Example | Description | Pipelines |
|---------|-------------|-----------|
| [python-basic](./python-basic/) | Python ETL with uv-managed deps | 3 |
| [sql-duckdb-basic](./sql-duckdb-basic/) | Local SQL analytics with DuckDB | 3 |
| [multi-group](./multi-group/) | Multi-file pipeline groups (Python + SQL + Docker) | 7 (3 groups) |

## Usage

```bash
cd python-basic
flowerpot validate
flowerpot run
```

```bash
cd sql-duckdb-basic
flowerpot validate
flowerpot run
```

## License

Apache 2.0
