import json

from llm import ask_llm
from tools.weather_tool import get_weather


scenario = """
A student named Arun has 5 hours available today.

Tasks:

1. DSA - 2 hours - High priority - Deadline tomorrow
2. SQL - 1.5 hours - Medium priority - Deadline in 2 days
3. Machine Learning - 2 hours - High priority - Deadline in 4 days
4. Java revision - 1 hour - Medium priority - Deadline in 3 days

The student is in Erode.

Question:
Which study tasks should Arun prioritize and is it practical
to include an outdoor study session today based on the current weather?
"""


print("\n===== ReACT AGENT =====\n")

# STEP 1: Thought
print("THOUGHT:")
decision_prompt = f"""
You are a reasoning agent.

Analyze the following scenario:

{scenario}

Determine whether current external weather information is
needed to answer the question.

If weather information is needed, respond exactly:

ACTION: WEATHER:Erode

Otherwise respond exactly:

ACTION: NONE
"""

decision = ask_llm(decision_prompt, temperature=0)

print(decision)


# STEP 2: Action
if "ACTION: WEATHER:Erode" in decision:

    print("\nACTION:")
    print("get_weather('Erode')")

    # STEP 3: Observation
    weather = get_weather("Erode")

    print("\nOBSERVATION:")
    print(json.dumps(weather, indent=4))

else:
    weather = None


# STEP 4: Final reasoning
if weather:
    weather_text = json.dumps(weather, indent=4)
else:
    weather_text = "No weather observation was available."


final_prompt = f"""
Answer the following scenario using the information provided.

Scenario:
{scenario}

External tool observation:
{weather_text}

Give:
1. The study tasks Arun should prioritize within 5 hours.
2. Whether an outdoor study session is practical.
3. A short reasoning summary.

Important:
- Use the weather observation only if it contains valid weather information.
- If the weather tool failed or returned an error, clearly state that
  current weather could not be verified.
- Do not invent weather information.
"""

print("\nFINAL ANSWER:")

answer = ask_llm(final_prompt, temperature=0)

print(answer)
