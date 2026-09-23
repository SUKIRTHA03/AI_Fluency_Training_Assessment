<<<<<<< HEAD
\# Agentic AI: Foundations and Open-Source Practice — Day 2



\## 1. Introduction



This assessment compares three prompting and agentic AI approaches: Direct Prompting, Chain-of-Thought (CoT), and ReAct. The same study-planning scenario was used to understand how each approach handles reasoning, task prioritization, and external information.



A Self-Consistency experiment was also performed by running the reasoning task five times at a non-zero temperature and observing whether the generated answers were consistent.



The implementation was developed in Python using the Groq API. The ReAct experiment additionally used an external weather tool.



\---



\## 2. Chosen Scenario



The scenario involved a student named Arun who has 5 hours available for studying today.



| Task             |  Duration | Priority | Deadline  |

| ---------------- | --------: | -------- | --------- |

| DSA              |   2 hours | High     | Tomorrow  |

| SQL              | 1.5 hours | Medium   | In 2 days |

| Machine Learning |   2 hours | High     | In 4 days |

| Java revision    |    1 hour | Medium   | In 3 days |



The question was:



> Which tasks should Arun prioritize within his 5 available hours?



For the ReAct experiment, an additional requirement was introduced: Arun is in Erode and wants to know whether an outdoor study session is practical based on current weather.



\---



\## 3. Prompting and Agentic Approaches



\### 3.1 Direct Prompting



Direct Prompting asks the language model to answer the question directly using the information supplied in the prompt. No external tools are used and no explicit multi-step reasoning process is required.



In this experiment, the model recommended:



\* DSA — 2 hours

\* Machine Learning — 2 hours

\* Java revision — 1 hour



This uses all 5 available hours and includes both high-priority tasks.



The model also explained that DSA has the nearest deadline and that Java revision fits the remaining one-hour slot, whereas SQL requires 1.5 hours.



\*\*Observed result:\*\* Direct Prompting produced a clear and usable schedule for the supplied information.



\---



\### 3.2 Chain-of-Thought



The Chain-of-Thought experiment asked the model to reason carefully about task priorities, durations, deadlines, and the available time before producing a final answer.



The implementation requested a short reasoning summary rather than private or hidden chain-of-thought.



The model again recommended:



\* DSA — 2 hours

\* Machine Learning — 2 hours

\* Java revision — 1 hour



The reasoning summary considered priority, deadline urgency, and whether each task could fit within the remaining time.



\*\*Observed result:\*\* The Chain-of-Thought approach produced the same recommendation as Direct Prompting, but provided a more structured explanation of the factors used to reach the recommendation.



\---



\### 3.3 ReAct



ReAct combines reasoning with actions and observations from external tools.



The implementation followed this sequence:



1\. \*\*Thought:\*\* Determine whether current weather information is required.

2\. \*\*Action:\*\* Call the weather tool for Erode.

3\. \*\*Observation:\*\* Read the result returned by the tool.

4\. \*\*Final Answer:\*\* Use the observation when available and avoid inventing information when the tool fails.



The actual experiment produced:



```text

THOUGHT:

ACTION: WEATHER:Erode



ACTION:

get\_weather('Erode')



OBSERVATION:

{

&#x20;   "city": "Erode",

&#x20;   "error": "Weather service timed out."

}

```



The weather service timed out during the experiment. The agent therefore stated that current weather could not be verified instead of inventing weather conditions.



\*\*Observed result:\*\* ReAct demonstrated the use of an external tool and showed how the agent can incorporate tool observations into its final response. It also demonstrated appropriate handling of a failed tool call.



\---



\## 4. Comparison of the Three Approaches



| Feature                      | Direct Prompting                | Chain-of-Thought                             | ReAct                                           |

| ---------------------------- | ------------------------------- | -------------------------------------------- | ----------------------------------------------- |

| Reasoning depth              | Basic                           | More structured multi-step reasoning         | Reasoning combined with actions                 |

| External tools               | No                              | No                                           | Yes                                             |

| Multi-step reasoning         | Moderate                        | Stronger                                     | Strong, especially with external information    |

| Transparency                 | Final answer is easy to inspect | Reasoning summary can be inspected           | Actions and observations can be inspected       |

| Speed                        | Generally fast                  | Can require more reasoning                   | Can be slower because of tool calls             |

| External/current information | Not available unless supplied   | Not available unless supplied                | Can retrieve external information through tools |

| Handling tool failures       | Not applicable                  | Not applicable                               | Can observe and report tool failures            |

| Best use case                | Straightforward questions       | Complex reasoning using supplied information | Tasks requiring reasoning plus external tools   |



The three approaches therefore differ mainly in whether they use structured reasoning and whether they can interact with external tools.



\---



\## 5. Self-Consistency Experiment



Self-Consistency was tested using the following setup:



\* Number of runs: 5

\* Temperature: 0.8

\* Same reasoning question for every run

\* The model was asked to return a standardized `CHOICE` and a short `REASON`



\### Actual Results



\*\*Run 1\*\*



```text

CHOICE: DSA, Machine Learning, SQL

```



\*\*Run 2\*\*



```text

CHOICE: DSA, ML, SQL

```



\*\*Run 3\*\*



```text

CHOICE: DSA, ML, SQL

```



\*\*Run 4\*\*



```text

CHOICE: DSA, Machine Learning, SQL

```



\*\*Run 5\*\*



```text

CHOICE: DSA, Machine Learning, SQL

```



The script reported:



```text

3 occurrence(s): DSA, Machine Learning, SQL

2 occurrence(s): DSA, ML, SQL

```



Therefore, the exact string majority was 3/5.



However, `ML` and `Machine Learning` refer to the same task. After normalizing the task name, all five runs selected the same task combination:



\*\*DSA + Machine Learning + SQL\*\*



This indicates strong semantic consistency across the five stochastic runs even though the wording varied slightly.



The experiment demonstrates why Self-Consistency can be useful: multiple generated solutions can be compared to identify a recurring answer rather than relying on one sampled response.



\---



\## 6. Suitability for the Chosen Scenario



For the basic study-planning problem, Direct Prompting is sufficient because all required information is already provided in the prompt.



Chain-of-Thought is useful when the task requires considering multiple factors such as priority, duration, available time, and deadlines. The reasoning summary makes those factors easier to inspect.



The ReAct approach becomes useful when the task requires information that is not contained in the original scenario. In this assessment, current weather information was required for the outdoor-study question. The agent therefore decided to call the weather tool.



The actual weather request timed out. Instead of assuming or fabricating weather conditions, the agent reported that the current weather could not be verified. This demonstrates an important property of tool-using agents: external information can improve an answer when available, but tool failures must also be handled safely.



\---



\## 7. Advantages and Limitations



\### Direct Prompting



\*\*Advantages:\*\*



\* Simple to implement

\* Fast

\* Requires no external tools

\* Works well when all information is already available



\*\*Limitations:\*\*



\* Cannot independently retrieve current external information

\* Less suitable for tasks requiring interaction with external systems



\### Chain-of-Thought



\*\*Advantages:\*\*



\* Encourages structured reasoning

\* Useful for multi-step problems

\* Produces a reasoning summary that can make the answer easier to understand



\*\*Limitations:\*\*



\* Still depends on the information supplied to the model

\* Does not independently retrieve external information



\### ReAct



\*\*Advantages:\*\*



\* Combines reasoning with tool usage

\* Can retrieve external information

\* Makes the action and observation process visible

\* Can respond appropriately when a tool fails



\*\*Limitations:\*\*



\* More complex to implement

\* Tool calls can increase latency

\* External services can fail, as demonstrated by the weather timeout



\---



\## 8. Conclusion



This assessment demonstrated three increasingly capable approaches to solving AI tasks.



Direct Prompting is appropriate when the problem is straightforward and all required information is already available. Chain-of-Thought is useful when the problem requires more structured multi-step reasoning. ReAct extends reasoning by allowing an agent to interact with external tools and use their observations when generating a final answer.



The Self-Consistency experiment showed that repeated sampling at temperature 0.8 produced slightly different wording but the same semantic task combination after normalization.



The ReAct experiment also demonstrated that external tools introduce failure possibilities. When the weather service timed out, the agent correctly avoided inventing weather information and reported that the information could not be verified.



Overall, the experiments show the progression from direct model responses, to structured reasoning, to reasoning combined with external actions and observations.



=======
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
>>>>>>> origin/main
