"""Load: read transformed data and produce a summary report."""

import json
import os
from collections import Counter

input_dir = os.environ.get("INPUT_DIR", "./data/transformed")

input_path = os.path.join(input_dir, "users_graded.json")
with open(input_path) as f:
    records = json.load(f)

grades = Counter(r["grade"] for r in records)
avg_score = sum(r["score"] for r in records) / len(records) if records else 0

print(f"[load] summary: {len(records)} users, avg score {avg_score:.1f}")
print(f"[load] grade distribution: {dict(grades)}")
print("[load] done")
