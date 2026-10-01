 Day 4 — Will It Fit, and May I Use It?

## 1. Scenario

### User and Use Case

I am evaluating open-weight language models for personal coding assistance and technical question answering on my laptop.

### Hardware

- Laptop: ASUS TUF Gaming A15 FA506NCR
- System RAM: approximately 16 GB
- Dedicated GPU memory: approximately 4 GB
- CPU: AMD Ryzen 7 7435HS
- GPU: NVIDIA GeForce RTX 3050 Laptop GPU

The main constraint is that the laptop has limited dedicated GPU memory. Larger models may therefore need system RAM or may not be practical for local use.

---

## 2. Memory Estimation Concepts

A model needs memory for several components.

### Model Weights

Model weights store the learned parameters of the model.

The approximate memory required for weights is:

```text
weights (GB) = parameters in billions × bytes per parameter
Quantization

Quantization stores model parameters using fewer bits/bytes.

The values used in this lab are:

Precision	Bytes per parameter
FP16/BF16	2.00
Q8_0	1.00
Q6_K	0.81
Q5_K_M	0.68
Q4_K_M	0.57
Q3_K_M	0.43

Lower-bit quantization reduces memory requirements, although the exact runtime behaviour can vary.

KV Cache

The KV cache stores information from the context during inference.

The lab provides this approximate formula:

KV cache (GB) = parameters in billions × context in K tokens × 0.02
Total Estimate

The lab adds 10% overhead:

total (GB) = (weights + KV cache) × 1.10

These values are estimates for checking whether a model may fit. They are not exact runtime memory measurements.

3. Memory Estimation Results

The following estimates use an 8K-token context unless otherwise stated.

Model	Precision	Weights	KV Cache	Total
1.5B	Q4_K_M	0.85 GB	0.24 GB	1.20 GB
8B	Q4_K_M	4.56 GB	1.28 GB	6.42 GB
8B	FP16	16.00 GB	1.28 GB	19.01 GB
30B	Q4_K_M	17.10 GB	4.80 GB	24.09 GB
70B	Q4_K_M	39.90 GB	11.20 GB	56.21 GB

The results show that model size and quantization have a large effect on memory requirements.

For example, an 8B model at Q4_K_M is estimated at 6.42 GB, while the same model at FP16 is estimated at 19.01 GB.

4. Context and Quantization Experiments
4.1 Context Length Experiment

For an 8B Q4_K_M model:

Context	Weights	KV Cache	Total
4K	4.56 GB	0.64 GB	5.72 GB
8K	4.56 GB	1.28 GB	6.42 GB
16K	4.56 GB	2.56 GB	7.83 GB
32K	4.56 GB	5.12 GB	10.65 GB

The weight memory stays constant, while the estimated KV-cache memory increases with context length.

Therefore, increasing the context window can significantly increase memory requirements.

4.2 Quantization Experiment

For an 8B model at 8K context:

Quantization	Weights	KV Cache	Total
FP16	16.00 GB	1.28 GB	19.01 GB
Q8_0	8.00 GB	1.28 GB	10.21 GB
Q6_K	6.48 GB	1.28 GB	8.54 GB
Q5_K_M	5.44 GB	1.28 GB	7.39 GB
Q4_K_M	4.56 GB	1.28 GB	6.42 GB
Q3_K_M	3.44 GB	1.28 GB	5.19 GB

Quantization mainly reduces the memory used by the model weights. The estimated KV cache remains the same in this simplified formula.

5. Model Comparison

Four model families were compared as required by the lab:

Qwen
Mistral
IBM Granite
gpt-oss
Field	Qwen3-4B	Mistral 7B	Granite 4:3B	gpt-oss:20b
Publisher	Qwen / Alibaba	Mistral AI	IBM	OpenAI
Parameters	4.0B / 4.02B	7.25B	3.4B	20.9B
Ollama size	2.5 GB	4.4 GB	2.1 GB	14 GB
Quantization	Q4_K_M	Q4_K_M	Q4_K_M	MXFP4
Context	32K native / 131K with YaRN	32K	128K	128K
Licence	Apache License 2.0	Apache License 2.0	Apache License 2.0	Apache License 2.0
Commercial use	Yes	Yes	Yes	Yes
Tool calling	Yes	Not verified	Yes	Not verified from supplied details
Ollama build	Yes	Yes	Yes	Yes
Approx. 8K memory estimate	3.21 GB	5.82 GB	2.72 GB	16.77 GB
Fit for 16 GB RAM	Yes, estimated	Yes, estimated	Yes, estimated	Above estimate
Qwen3-4B

Qwen3-4B has approximately 4 billion parameters. The Ollama Q4_K_M build is approximately 2.5 GB.

The model card describes tool and agentic capabilities. It gives 32,768 native context and up to 131,072 with YaRN.

Using 4.0B parameters, Q4_K_M and 8K context:

Weights = 4.0 × 0.57 = 2.28 GB
KV      = 4.0 × 8 × 0.02 = 0.64 GB
Total   = (2.28 + 0.64) × 1.10
        ≈ 3.21 GB

The licence is Apache License 2.0.

Mistral 7B

The Ollama page lists Mistral 7B at approximately 4.4 GB, with 7.25B parameters and Q4_K_M quantization. The listed context window is 32K.

Using 7.25B parameters, Q4_K_M and 8K context:

Weights = 7.25 × 0.57 = 4.13 GB
KV      = 7.25 × 8 × 0.02 = 1.16 GB
Total   = (4.13 + 1.16) × 1.10
        ≈ 5.82 GB

The Ollama details identify Apache License Version 2.0.

Tool-calling information was not verified from the supplied Mistral model-card material.

Granite 4:3B

Granite 4:3B is an IBM model with 3.4B parameters. The Ollama page lists a 2.1 GB Q4_K_M build and a 128K context window.

The supplied Granite information states that the model has improved instruction following and tool-calling capabilities. It also lists code-related tasks and function-calling tasks.

Using 3.4B parameters, Q4_K_M and 8K context:

Weights = 3.4 × 0.57 = 1.94 GB
KV      = 3.4 × 8 × 0.02 = 0.54 GB
Total   = (1.94 + 0.54) × 1.10
        ≈ 2.72 GB

The licence is Apache License 2.0.

gpt-oss:20b

The Ollama page lists gpt-oss:20b at approximately 14 GB with a 128K context window.

The Ollama details list:

20.9B parameters
MXFP4 quantization
Apache License Version 2.0

Using the lab's simplified 0.57 value for a rough comparison:

Weights = 20.9 × 0.57 ≈ 11.91 GB
KV      = 20.9 × 8 × 0.02 ≈ 3.34 GB
Total   ≈ (11.91 + 3.34) × 1.10
        ≈ 16.77 GB

This is only a rough comparison because MXFP4 is not the same as Q4_K_M. Actual runtime memory can differ.

6. Estimate Versus Reality

Ollama was not available on this laptop.

The Windows Ollama download did not complete successfully. Therefore, the following commands could not be collected:

ollama list
ollama ps

Because of this, there is no actual local runtime measurement for this assessment.

I have not invented an ollama ps result.

The memory numbers in this report are therefore estimator results only.

Estimated memory and actual runtime memory can differ because of context length, quantization details, model architecture and runtime overhead.

The 8B Q4_K_M estimate of 6.42 GB is below the laptop's approximately 16 GB system RAM, but it is above the approximately 4 GB dedicated GPU memory. This does not prove how an actual runtime would split memory between CPU and GPU.

7. Suitability for My Laptop

My scenario is personal coding assistance and technical question answering.

The main hardware constraints are:

Approximately 16 GB system RAM
Approximately 4 GB dedicated GPU memory
Limited dedicated GPU memory for larger models
Selected Model

Granite 4:3B, Q4_K_M, 128K context, Apache License 2.0

The estimated memory requirement at 8K context is approximately 2.72 GB.

The supplied Granite information also describes instruction following, tool calling, code-related tasks and function-calling tasks.

Runner-up

Qwen3-4B, Q4_K_M, Apache License 2.0

The estimated 8K memory requirement is approximately 3.21 GB.

The Qwen3 model card describes tool and agentic capabilities.

Scenario Change

If the available system memory were increased substantially, a larger model such as gpt-oss:20b could become more practical to evaluate locally.

The recommendation would therefore depend on the available hardware and memory budget.

8. Memory-Decides and Licence-Decides Cases
Memory-decides case

If two models have similar capabilities and licences but one requires substantially more memory, available RAM and GPU memory become important factors when deciding which model can practically be evaluated locally.

For this laptop, the difference between a roughly 3 GB estimate and a roughly 17 GB estimate is significant.

Licence-decides case

If two models have similar memory requirements but different licences, the licence terms should be checked before commercial use or redistribution.

The selected Qwen, Mistral, Granite and gpt-oss models are identified with Apache License 2.0 in the supplied model information.

Apache License 2.0 permits commercial use, subject to its licence conditions.

The exact licence should always be checked on the current model card before deployment.

9. Key Findings
Model parameter count has a major effect on memory requirements.
Quantization can significantly reduce model-weight memory.
Increasing context length increases estimated KV-cache memory.
An Ollama download size is not the same as total runtime memory.
The lab's memory formula is an estimate rather than an exact runtime measurement.
Smaller quantized models are more practical to evaluate on a laptop with limited memory.
Tool calling can be useful for agentic and coding workflows.
Model licences must be checked separately from technical fit.
Actual runtime measurements could not be collected because Ollama was unavailable.
10. Conclusion

This assessment shows why model selection is not based only on parameter count.

Memory depends on the number of parameters, quantization, context length, KV cache and runtime overhead.

For my laptop, the estimates show a large difference between smaller quantized models and larger models. Granite 4:3B and Qwen3-4B have substantially lower estimated memory requirements than gpt-oss:20b.

The final choice should consider:

Model size
Quantization
Context length
Required capabilities
Tool calling
Licence conditions
Available RAM and GPU memory
Actual runtime measurements

Ollama could not be installed during this assessment, so actual ollama list and ollama ps measurements were not available. The runtime section therefore uses estimates only and does not claim that an unmeasured model was successfully run locally.

11. Sources
Qwen
Hugging Face: https://huggingface.co/Qwen/Qwen3-4B
Ollama: https://ollama.com/library/qwen3
Apache License 2.0: https://www.apache.org/licenses/LICENSE-2.0
Mistral
Hugging Face: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
Ollama: https://ollama.com/library/mistral
IBM Granite
Hugging Face: https://huggingface.co/ibm-granite
Ollama: https://ollama.com/library/granite4
Granite documentation: https://www.ibm.com/granite/docs
Granite GitHub: https://github.com/ibm-granite/granite-4.0-language-models
gpt-oss
Hugging Face: https://huggingface.co/openai
Ollama: https://ollama.com/library/gpt-oss
Assessment Method

The memory calculations use the formula and bytes-per-parameter values provided in the Day 4 lab manual.