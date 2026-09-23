from collections import Counter
from llm import ask_llm

question = """
Arun has 6 hours available.

Tasks:

DSA:
2 hours
High priority
Deadline tomorrow

SQL:
1.5 hours
Medium priority
Deadline in 2 days

Machine Learning:
2 hours
High priority
Deadline in 4 days

Java:
1 hour
Medium priority
Deadline in 3 days

Which combination of tasks should Arun complete within 6 hours
if he wants to prioritize urgency and high-priority tasks?

Return your answer in this exact format:

CHOICE: <task combination>
REASON: <one short sentence>
"""

answers = []

print("\n===== SELF-CONSISTENCY EXPERIMENT =====")
print("Temperature: 0.8")
print("Number of runs: 5\n")

for i in range(5):
    answer = ask_llm(question, temperature=0.8)
    answers.append(answer)

    print(f"--- Run {i + 1} ---")
    print(answer)
    print()

choices = []

for answer in answers:
    for line in answer.splitlines():
        if line.strip().upper().startswith("CHOICE:"):
            choice = line.split(":", 1)[1].strip()
            choices.append(choice)
            break

print("===== MAJORITY ANALYSIS =====")

counts = Counter(choices)

for choice, count in counts.items():
    print(f"{count} occurrence(s): {choice}")

if counts:
    majority_choice, majority_count = counts.most_common(1)[0]

    print("\nMajority answer:")
    print(majority_choice)
    print(f"Frequency: {majority_count}/5")
else:
    print("Could not extract standardized choices.")