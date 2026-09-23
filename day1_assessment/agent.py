import json

# ---------------- TOOLS ----------------

def read_private_tasks():
    with open("private_data.json", "r", encoding="utf-8") as f:
        return json.load(f)


def get_pending_tasks(data):
    return [task for task in data["tasks"]
            if task["status"] == "Pending"]


# ---------------- LLM REASONING ----------------
# This lightweight local function represents the LLM's decision-making
# so the demonstration can run without an external API.

def llm_reason(user_request, tasks):
    high_priority = [
        task for task in tasks
        if task["priority"] == "High"
    ]

    if "study first" in user_request.lower():
        if high_priority:
            return (
                "The user wants to know what to study first. "
                "I should prioritize the pending High-priority tasks."
            )

    return "I should use the available private task information to answer."


# ---------------- AGENT LOOP ----------------

def agent(user_request):

    print("========== AI AGENT ==========\n")

    print("User:")
    print(user_request)

    print("\n--- LOOP 1 ---")
    print("LLM Reasoning:")
    print("I need information from the user's private study data.")

    print("\nTool selected: read_private_tasks()")
    data = read_private_tasks()

    print("Tool result: Private study data received.")

    print("\n--- LOOP 2 ---")
    print("LLM Reasoning:")
    print("I should filter the data to find pending tasks.")

    print("\nTool selected: get_pending_tasks()")
    pending = get_pending_tasks(data)

    print("Tool result:")
    for task in pending:
        print(
            f"- {task['task']} | "
            f"{task['priority']} | "
            f"{task['status']}"
        )

    print("\n--- LOOP 3 ---")
    reasoning = llm_reason(user_request, pending)
    print("LLM Reasoning:")
    print(reasoning)

    high_priority = [
        task for task in pending
        if task["priority"] == "High"
    ]

    print("\n--- FINAL ANSWER ---")

    if high_priority:
        print("Based on the private task data, you should start with:")
        for task in high_priority:
            print(
                f"- {task['task']} ({task['subject']}, "
                f"{task['hours']} hours)"
            )

        print("\nAfter completing the high-priority DSA tasks,")
        print("you can continue with SQL and then OS.")

    print("\n========== AGENT COMPLETED ==========")


if __name__ == "__main__":
    agent("What should I study first from my private task list?")