# Rule-based workflow: reads private data and follows fixed if/else rules.
import json

def workflow():
    with open("private_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    pending = [t for t in data["tasks"] if t["status"] == "Pending"]
    order = {"High": 1, "Medium": 2, "Low": 3}
    pending.sort(key=lambda t: (order[t["priority"]], t["hours"]))

    print("Rule-Based Workflow Response:")
    print("Private data accessed: YES")
    print("Fixed rules: Pending tasks -> High -> Medium -> Low")
    print("\nRecommended tasks:")
    for t in pending:
        print(f"- {t['task']} ({t['subject']}, {t['priority']}, {t['hours']}h)")

if __name__ == "__main__":
    workflow()
