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
Explain the final recommendation briefly.
"""

prompt = f"""
Answer the following question directly using only the information provided.

Do not use external tools.

{scenario}
"""

answer = ask_llm(prompt, temperature=0)

print("\n===== DIRECT PROMPTING =====\n")
print(answer)