"""Transform: read raw data, apply business logic, write clean output."""

import json
import os

from tabulate import tabulate

input_dir = os.environ.get("INPUT_DIR", "./data/raw")
output_dir = os.environ.get("OUTPUT_DIR", "./data/transformed")
os.makedirs(output_dir, exist_ok=True)

input_path = os.path.join(input_dir, "users.json")
with open(input_path) as f:
    records = json.load(f)

transformed = []
for r in records:
    transformed.append({
        "id": r["id"],
        "name": r["name"].upper(),
        "score": r["score"],
        "grade": "A" if r["score"] >= 90 else "B" if r["score"] >= 80 else "C",
        "ts": r["ts"],
    })

output_path = os.path.join(output_dir, "users_graded.json")
with open(output_path, "w") as f:
    json.dump(transformed, f, indent=2)

print(f"[transform] processed {len(transformed)} records")
print(tabulate(
    [(r["name"], r["score"], r["grade"]) for r in transformed],
    headers=["Name", "Score", "Grade"],
    tablefmt="simple",
))
