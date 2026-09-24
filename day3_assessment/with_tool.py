import os
import json
from groq import Groq
from dotenv import load_dotenv
from tool import get_weather

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current temperature for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

question = "What is the current temperature in Erode?"

messages = [
    {"role": "user", "content": question}
]

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message

print("Question:", question)
print("Tool call:", message.tool_calls)

if message.tool_calls:
    messages.append({
        "role": "assistant",
        "content": message.content,
        "tool_calls": [
            {
                "id": call.id,
                "type": "function",
                "function": {
                    "name": call.function.name,
                    "arguments": call.function.arguments
                }
            }
            for call in message.tool_calls
        ]
    })

    for tool_call in message.tool_calls:
        args = json.loads(tool_call.function.arguments)

        result = get_weather(args["city"])

        print("Tool result:", result)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })

    final_response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages
    )

    print("Final answer:", final_response.choices[0].message.content)
else:
    print("No tool call was made.")
    print("LLM answer:", message.content)