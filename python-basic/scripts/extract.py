"""Extract: fetch sample data and write to raw files."""

import json
import os
from datetime import datetime, timezone

output_dir = os.environ.get("OUTPUT_DIR", "./data/raw")
os.makedirs(output_dir, exist_ok=True)

records = [
    {"id": 1, "name": "Alice", "score": 85, "ts": "2026-04-01T10:00:00Z"},
    {"id": 2, "name": "Bob", "score": 92, "ts": "2026-04-01T11:00:00Z"},
    {"id": 3, "name": "Charlie", "score": 78, "ts": "2026-04-01T12:00:00Z"},
    {"id": 4, "name": "Diana", "score": 95, "ts": "2026-04-02T09:00:00Z"},
    {"id": 5, "name": "Eve", "score": 88, "ts": "2026-04-02T14:00:00Z"},
]

output_path = os.path.join(output_dir, "users.json")
with open(output_path, "w") as f:
    json.dump(records, f, indent=2)

print(f"[extract] wrote {len(records)} records to {output_path}")
print(f"[extract] run at {datetime.now(timezone.utc).isoformat()}")
