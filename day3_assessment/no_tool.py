import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

question = "What is the current temperature in Erode?"

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "user", "content": question}
    ]
)

print("Question:", question)
print("LLM answer:", response.choices[0].message.content)