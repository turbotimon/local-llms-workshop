---
theme: ost
paginate: true
marp: true
html: true
title: "Local LLMs"
header: "OSS Meetup - Local LLMs"
footer: "Timon Erhart &nbsp;| &nbsp; [OST Ostschweizer Fachhochschule](https://www.ost.ch)"
backgroundImage: ./theme/image1.jpg
---

<!-- _class: lead -->
<!-- _paginate: skip # skip the header -->
<!-- _header: "" # skip the footer -->
<!-- _footer: "" # skip the footer -->

<style scoped>
  * {
    background-color: rgba(255, 255, 255, 0.3);
  }
</style>

![bg cover](./theme/image2.jpg)

# Local LLMs

### OSS Meetup

2026-11-10 Timon Erhart

---

## Ingredients

<!-- AGENT
Create a mermaid diagram in a separate ingredients.md file. then export it as sgv and include it here.
It should be a simple diagram showing the process
Hardware(CPU, GPU,RAM) -> Inference Engine (llama.cpp, vLLM, MLX, ...) -> 
Model Runner (Ollama, LM Studio, ...) -api-> Applications [
  SDK's (Pydantic AI, LangGraph, OpenAI SDK),
  Coding Agents (OpenCode, Pi, Claude Code, ...),
  Apps (Open WebUI, OpenClaw, Docling),
]

Use simple icons for every component. Thinks in the brackets are example, they should appear exactly like that (do not leave out or expand)

Use colors defined in theme/ost.css

-->

---

## Formats

<!-- AGENT
List/Explain most popular formats:
- GGUF
- Safetensors

As well as precisions & Quantization:
- FP32
- BF16
- Q8_0
- Q4_K_M
- Q2_K

--> 

---

## Ollama

Ollama is a local LLM runner that provides a CLI and API interface.

- Get started: https://docs.ollama.com/quickstart

Supported API endpoints:

- Ollama API: http://localhost:11434/api
- OpenAI Chat Completions: http://localhost:11434/v1
- OpenAI Responses: https://ollama.com/v1/responses
- Anthropic Messages: http://localhost:11434
- System One (decisions): http://localhost:11434/v1/systemone

We will use the OpenAI Chat Completions in this workshop

---

## Usage 1: Raw API


```sh
curl https://ollama.com/v1/chat/completions \
  # Not needed for local calls
  # -H "Authorization: Bearer $OLLAMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:31b",
    "messages": [
      {
        "role": "user",
        "content": "Say hello in one sentence."
      }
    ]
  }'
```

<!-- AGENT

Do not change this slide but refer workshp/01_api

In workshp/01_api/

create a simple markdown on how to curl to ollama.

it starts with the above example and then

give the attendees these tasks to step-by-step improve the curl command:
- change the model to: a model that runs fine on their hardware with the following capabilities: reasoning, tools, vision
- explore models thinking capability and use them : https://docs.ollama.com/capabilities/thinking
- force structured JSON output
- include an image: https://docs.ollama.com/capabilities/vision

For the above task, a nice to problem spanning the whole list would be nice. e.g. what is the capital of Switzerland? reasoning: why some people think the capital of switzerland is zurich? for image: which city is show in the image (i will provide bern.jpg)

In workshop/01_api/decision.md

as user to:
- download a decision model
- test it out by reading: https://docs.ollama.com/capabilities/decision

In general: If links are given in the above bullet points, do not read them and explain the content. but give the link and attendess should figure out on their own from the docs

--> 

## LM Studio

LM Studio is a local LLM runner that provides a **GUI and API interface**. It provide the same features like Ollama and some more

- Model management
- Customization
- Tool usage (MCP)
- Chat
- 

Like Ollama, several API endpoints are supported.

The rather new Bionic provides even more features similar do e.g. Claude Desktop: for creativity, work, and code

---

## Usage 2: Python SDK & Tools

<!-- AGENT

In workshp/02_sdk

Create a minimal app_xx.py that uses Pythantic sdk:

First, create pyproject.toml on root. we will us uv to install it

For the app_xx.py where xx is:
01: simple example that uses the SDK to call a model and get a response: prompt should be "You are MC LMM, only answer in sweet rap rimes: What time is it?"
02: settings like system prompt, temperature, top_p, reasoning etc., find 2 more
03: tool usage with simple get_time tool. then ask the model should be asked what time it is?
04: Optional: they should explore them selves how to sent images to them. Provide the solution as app04_SOLUTION.py 

The following numbers always have the solution from the previous, so users can continue even if not finish
It should use the URL provides from LM Studio

If other requirements are needed, you can add them, but please only if they really are needed and keep it short

--> 

---

## Usage 3: Agent Harnesses

<!-- AGENT

In workshp/03_harnesses

create a markdown.md , ask them to install opencode , provide minimal starting settings to include the url and most used settings.

then ask them to start the agent in the current folder 03_harnesses and let the agent code a simple python script that uses https://open-meteo.com/en/docs and provide the following function `get_temperature(city: str) -> float` that returns the current temperature in celsius for a given city. Add requests to the requirments and tell attendes to use requests

--> 

---

## Using an MCP

<!-- AGENT

In workshp/04_use_mcp/

mcp1.md:

Ask users to create an account for context7, create an API key and include the mcp to opencode (provide the setting snipped). Then they need to explore with opencode if it can use it.

then in mcp2.md:

ask them to install an mcp locally and include them as well. Any good ideas for an good or funny mcp that does not need a lot of setup and is easy to use, yet safe?

https://github.com/modelcontextprotocol/servers/tree/main/src/fetch

--> 

---

## Creating your own MCP

https://github.com/modelcontextprotocol

<!-- AGENT

In workshp/05_create_mcp/weather_mcp.md:

Using FastMCP, create the scaffold for them to add the `get_temperature(city: str) -> float` function (it should be as a side modul/solution weather_api.py) as an mcp. Then they should include run the mcp and include it e.g. in lm studio and ask "Do you think it is good weather to go for a swim in lake zurich near Rapperswil?"

Make sure the FastMCP logs/prints all calls, so they can see what happens

--> 

---

## Local RAG

RAG (Retrieval Augmented Generation) is a technique to include relevant external information into the LLM to improve the quality of the generated output.

The simplified pipeline is:

1. Chunk the documents (text, pdf, html, ...)
2. Create embeddings for each chunk
3. Store the embeddings in a vector store (Chroma, LanceDB, ...)
4. When a user query comes in, create an embedding for the query
5. Retrieve the most relevant chunks by doing a similarity search of the embeddings in the vector store
6. Prompt the LLM including the query and retrieved chunks to generate a response

<!-- IDEA

minimal code (best for teaching how RAG works)

LLM + embeddings: Ollama, which serves both chat and embedding models behind one API
Embedding model: nomic-embed-text, bge-m3, or EmbeddingGemma
Vector store: Chroma (simplest, pip install, no server); alternatives are LanceDB or sqlite-vec
Glue: plain Python, about 50 lines (chunk, embed, store, retrieve, prompt); this makes every step visible
Optional framework: LlamaIndex is the simplest if you want less code
Parsing: pypdf for simple PDFs, Docling for complex layouts
Optional UI: Gradio or Streamlit

-->

---

## Aftermath

Things explicitly not covered, but you should read about if you are not familiar with:

- How does an LLM work (transformer, embeddings, auto-regressive, attention, etc.)
- AGENTS.md and SKILL.md files
- Settings like temperature, top_p
- LLM Security and guardrails
- Prompt engineering

Thinks to explore yourself:

- Install and use **Open WebUI**
- The full capabilities of agent SDK's (e.g. guardrails, subagents, ...)
- Build simple frontends and Apps using streamlit or gradio