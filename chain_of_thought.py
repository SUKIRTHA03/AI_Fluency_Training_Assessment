from llm import ask_llm

scenario = """
A student named Arun has 5 hours available today.

Tasks:

1. DSA - 2 hours - High priority - Deadline tomorrow
2. SQL - 1.5 hours - Medium priority - Deadline in 2 days
3. Machine Learning - 2 hours - High priority - Deadline in 4 days
4. Java revision - 1 hour - Medium priority - Deadline in 3 days

Question:
Which tasks should Arun prioritize within his 5 available hours?
"""

prompt = f"""
Solve the following problem carefully.

Reason through the priorities, available time, task durations,
and deadlines before giving your answer.

Do not use any external tools.

Give:
1. Final recommendation
2. A short reasoning summary explaining the important factors

Do not provide private chain-of-thought or hidden reasoning.

Problem:
{scenario}
"""

answer = ask_llm(prompt, temperature=0)

print("\n===== CHAIN-OF-THOUGHT =====\n")
print(answer)