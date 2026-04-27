"""Extract sample event data and write to JSON."""

import json
import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "./data/raw"))

SAMPLE_EVENTS = [
    {"id": 1, "user": "Alice", "event": "Purchase", "amount": 42.50},
    {"id": 2, "user": "Bob", "event": "Signup", "amount": 0},
    {"id": 3, "user": "Charlie", "event": "Purchase", "amount": 119.99},
    {"id": 4, "user": "alice", "event": "Refund", "amount": -42.50},
    {"id": 5, "user": "Diana", "event": "Purchase", "amount": 75.00},
]


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "events.json"
    with open(out_path, "w") as f:
        json.dump(SAMPLE_EVENTS, f, indent=2)
    print(f"Extracted {len(SAMPLE_EVENTS)} events -> {out_path}")


if __name__ == "__main__":
    main()
