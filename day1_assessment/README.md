# Agentic AI: Foundations and Open-Source Practice — Day 1

## Scenario
A student has a private JSON file containing personal study tasks. The user asks:
**"What should I study first from my private task list?"**

The same request is implemented using:
1. Plain chatbot
2. Rule-based workflow
3. AI agent

## Run

### Plain chatbot
```bash
python chatbot.py
```

### Rule-based workflow
```bash
python workflow.py
```

### AI agent
Install/start Ollama and pull a model:
```bash
ollama run llama3.2
```
Then:
```bash
python agent.py
```

The agent demonstrates the pattern **LLM + Tools + Loop**:
- LLM reasons about the request.
- Tools read and filter private data.
- The agent observes tool results.
- The loop continues until it can produce the final answer.

## Output
Put screenshots of the three runs in `Output/`.
