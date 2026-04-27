"""Normalize extracted events: lowercase user names, validate amounts."""

import json
import os
from pathlib import Path

INPUT_DIR = Path(os.environ.get("INPUT_DIR", "./data/raw"))
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "./data/normalized"))


def normalize(events):
    cleaned = []
    for e in events:
        cleaned.append(
            {
                "id": e["id"],
                "user": str(e.get("user", "")).lower().strip(),
                "event": str(e.get("event", "")).lower().strip(),
                "amount": round(float(e.get("amount", 0)), 2),
            }
        )
    return cleaned


def main():
    in_path = INPUT_DIR / "events.json"
    with open(in_path) as f:
        raw = json.load(f)

    cleaned = normalize(raw)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "events_clean.json"
    with open(out_path, "w") as f:
        json.dump(cleaned, f, indent=2)

    print(f"Normalized {len(cleaned)} events -> {out_path}")


if __name__ == "__main__":
    main()
