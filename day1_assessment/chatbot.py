# Plain chatbot: LLM-style response with NO private-data tool.
# For this demo, the response is simulated so it runs without an API key.

def chatbot(user_request):
    return (
        "Plain Chatbot Response:\n"
        "I can suggest a study plan based on the information in your message, "
        "but I cannot inspect your private study_tasks JSON file because no "
        "private-data tool is connected.\n\n"
        f"User request: {user_request}\n"
        "Suggestion: Prioritize high-priority DSA work, then SQL, then OS."
    )

if __name__ == "__main__":
    print(chatbot("What should I study first from my private task list?"))
