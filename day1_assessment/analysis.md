# Day 1 — Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

For this task, I selected a personal study-planning scenario. My private data is stored in `private_data.json`, which contains study tasks, subjects, priorities, status, and estimated study hours. The user request is: **“What should I study first from my private task list?”**

The same request is handled in three different ways: a plain chatbot, a rule-based workflow, and an AI agent. This makes the differences between the three approaches clear.

## 2. Plain Chatbot

The plain chatbot mainly uses an LLM to understand the user's message and generate a natural-language response. In this implementation, no private-data tool is connected to the chatbot. Therefore, the chatbot cannot inspect `private_data.json` by itself. It can only use information supplied directly in the conversation or information already available to its model.

The chatbot requires no external tools or predefined decision rules. It receives the user's request, processes the text with the language model, and generates a response. It does not independently read files, perform actions, or repeatedly check the result of an action.

For this scenario, the limitation is private-data access. If the user asks which task should be studied first but does not provide the contents of the private task list, the chatbot cannot reliably know the actual pending tasks. It may give a general suggestion, but it cannot base the answer on the student's real private data.

## 3. Rule-Based Workflow

The rule-based workflow uses predefined programming rules rather than an LLM. In this implementation, the program directly reads `private_data.json`, keeps only pending tasks, and sorts them using fixed priority rules: High priority first, then Medium, then Low.

The workflow therefore has access to the private data because a file-reading operation is explicitly programmed. Its steps are predictable: read the file, filter pending tasks, sort by predefined priority, and display the result. There is no LLM reasoning or dynamic tool selection.

This approach works well when the problem is clearly defined and the rules are known in advance. However, its limitation is flexibility. If the user changes the request to something such as “choose tasks that fit into exactly three hours and focus on DSA,” the workflow needs additional manually written rules. It cannot dynamically decide which tool or action is appropriate.

## 4. AI Agent

The AI agent follows the pattern **LLM + Tools + Loop**. The LLM is responsible for understanding the user's request and deciding what information is needed. Tools provide access to the private study data. The agent observes the result of the tools and continues the loop until it has enough information to produce a final answer.

In this implementation, the first tool reads the private JSON file and the second tool filters the pending tasks. The agent then sends the observed private-data context to the local Ollama LLM, which reasons about the user's request and produces a study recommendation.

The important difference is that the agent is not just generating a response. It can interact with tools, observe their results, and continue taking steps. This makes it more suitable for multi-step tasks. Its limitations are greater complexity, dependency on tools and the LLM, and the possibility of incorrect decisions or outputs if the model or tool results are unreliable.

## 5. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | High for conversation, but limited by available context | Low to medium because rules are fixed | High because the LLM can adapt its reasoning |
| Decision-making | Generates a response from the conversation | Uses predefined conditions | LLM reasons and selects actions/tools |
| Tool usage | None in this scenario | Directly programmed file access | Uses tools selected as part of an agent loop |
| Private-data access | No direct access in this implementation | Yes, through programmed file reading | Yes, through tools |
| Multi-step task handling | Limited | Possible only through predefined steps | Stronger because the loop can continue based on observations |
| Automation | Mainly response generation | Good for fixed repetitive processes | Good for dynamic multi-step processes |
| Reliability | Predictable only when enough context is supplied | High for simple fixed rules | Depends on both tools and LLM decisions |

## 6. Suitability Analysis

For this particular scenario, the AI agent is the most suitable when the study-planning request can become dynamic or multi-step. The agent can access the private task data through tools, interpret the user's natural-language request, and use the observed information to decide what to do next. This is more flexible than a fixed workflow.

However, the rule-based workflow is also suitable when the requirement is simple and predictable, such as always showing pending High-priority tasks first. It is easier to test because the same input and rules produce predictable behavior. A plain chatbot is suitable when the user mainly wants general explanations or suggestions and does not need direct access to private data.

Therefore, the choice depends on the task requirements rather than simply choosing one technology for every problem.

## 7. Conclusion

A plain chatbot is appropriate for conversational tasks where the required information is already available in the conversation and no external action is required. It is simple and useful for answering questions, explaining concepts, and generating text.

A rule-based workflow is appropriate for predictable and repetitive tasks where the conditions and steps can be written clearly in advance. It provides controlled and repeatable behavior but becomes harder to maintain when the number of possible situations increases.

An AI agent is appropriate for tasks that require dynamic decision-making, private-data access through tools, multiple steps, and adaptation based on intermediate results. Its key idea is **LLM + Tools + Loop**: the LLM reasons about the task, tools provide access to information or actions, and the loop allows the agent to observe results and continue until the task is completed.

The three approaches are therefore useful for different problem types. The important distinction is that a chatbot mainly generates responses, a rule-based workflow follows predefined logic, and an AI agent combines reasoning, tools, and an iterative loop to handle more dynamic tasks.
