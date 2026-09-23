from llm import ask_llm

answer = ask_llm(
    "Reply with exactly: Groq connection successful.",
    temperature=0
)

print(answer)