"""Simple scoring model: read normalized events and produce scores."""

import json
from pathlib import Path

DATA_DIR = Path("/data")
INPUT_PATH = DATA_DIR / "normalized" / "events_clean.json"
OUTPUT_PATH = DATA_DIR / "scores.json"


def score(events):
    scores = []
    for e in events:
        value = 1.0 if e["event"] == "purchase" else 0.5
        value *= max(0, e["amount"]) / 100.0
        scores.append({"user": e["user"], "score": round(value, 4)})
    return scores


def main():
    with open(INPUT_PATH) as f:
        events = json.load(f)

    results = score(events)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Scored {len(results)} events -> {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
