import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing from .env")

if not MODEL:
    raise ValueError("MODEL is missing from .env")

client = Groq(api_key=api_key)


def ask_llm(prompt, temperature=0.0):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature
    )

    return response.choices[0].message.content