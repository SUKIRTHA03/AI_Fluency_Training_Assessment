\# From Prompt to Action: Understanding LLMs, Tools, and Agents



\## 1. Scenario



For this task, I chose a simple weather-related scenario.



The main question used for the demonstration was:



> What is the current temperature in Erode?



This question is useful for comparing a plain LLM with an LLM that has access to an external tool because the current temperature is information that changes over time and cannot reliably be answered from the model's stored knowledge.



I also considered questions such as:



\- What is 25 + 35?

\- What is the capital of France?



These questions can normally be answered directly by an LLM without requiring an external tool.



\---



\## 2. What is an LLM?



A Large Language Model (LLM) is a machine learning model trained on large amounts of text to understand and generate human-like language.



An LLM can confidently answer many questions involving general knowledge, explanations, writing, summarization, and reasoning based on information learned during training.



However, an LLM does not automatically have access to live information from the outside world. For example, current weather, live prices, or other changing information may not be available to it.



An LLM can also sometimes produce an answer that sounds correct even when the information is incorrect or uncertain. Therefore, external tools can be useful when accurate and current information is required.



In my experiment, the plain LLM was asked:



> What is the current temperature in Erode?



The LLM responded:



> I’m sorry, but I don’t have access to real-time weather data.



This demonstrated that the plain LLM did not have access to current weather information.



\---



\## 3. What is an Agent?



An agent is a system that uses an LLM to decide what action should be taken to complete a task.



A plain chat interaction mainly consists of:



> User → LLM → Answer



An agent can involve additional steps:



> User → LLM → Tool → Tool Result → LLM → Final Answer



The LLM can decide that an external tool is needed, request the tool call, receive the result, and then use that result to produce the final response.



In this task, the weather tool allowed the LLM to obtain the current temperature instead of relying only on its stored knowledge.



\---



\## 4. What is a Tool and Tool Call?



A tool is an external function that an LLM can request to perform an operation or obtain information that it cannot reliably provide by itself.



In this project, the tool was:



`get\_weather`



The tool was given a description and a parameter called `city`.



The tool schema contained:



\- \*\*Name:\*\* `get\_weather`

\- \*\*Description:\*\* Get the current temperature for a city.

\- \*\*Parameter:\*\* `city`

\- \*\*Parameter type:\*\* string



The schema is important because it tells the model what the tool does and what information it needs to provide when calling it.



For example, the model generated the following tool call:



```text

get\_weather({"city":"Erode"})

