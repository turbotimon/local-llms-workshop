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

## Roadmap



## Ingredients

Let's cook... 👨‍🍳

![h:470](./resources/ingredients.svg)

---

## Formats

<style scoped>
table { font-size: 0.75em; }
</style>

- **Safetensors** – raw training weights (vLLM, MLX)
- **GGUF** – one file, quantized (llama.cpp, Ollama, LM Studio)

| Precision | 8B model | Quality |
|-----------|----------|---------|
| FP32      | ~32 GB   | reference |
| BF16      | ~16 GB   | ≈ original |
| Q8_0      | ~8.5 GB  | almost lossless |
| Q4_K_M    | ~5 GB    | good – common default |
| Q2_K      | ~3 GB    | noticeably worse |

Model + context must fit into (V)RAM

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

Workshop: `workshop/01_api/`

---

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

- Agent SDKs (e.g. **Pydantic AI**) talk to any OpenAI-compatible server
- LM Studio: `http://localhost:1234/v1`
- **Tools** = Python functions the model can decide to call
- Steps: prompt → settings → tools → images

Workshop: `workshop/02_sdk/` (`uv sync`, then `uv run ...`)

---

## Usage 3: Agent Harnesses

- A harness turns a model into an agent: read files, run commands, edit code
- **OpenCode** – open source, works with local models
- Task: let the agent write `get_temperature(city: str) -> float`

Workshop: `workshop/03_harnesses/`

---

## Using an MCP

- **MCP** (Model Context Protocol) – standard to plug tools into any LLM app
- **Remote** MCP: hosted, e.g. Context7 (up-to-date docs)
- **Local** MCP: runs on your machine, e.g. fetch (`uvx mcp-server-fetch`)

Workshop: `workshop/04_use_mcp/`

---

## Creating your own MCP

https://github.com/modelcontextprotocol

- **FastMCP**: a Python function + `@mcp.tool` = MCP tool
- Name, type hints and docstring tell the LLM how to use it
- Connect it to LM Studio or OpenCode and watch the logs

Workshop: `workshop/05_create_mcp/`

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

Workshop: `workshop/08_rag/` – Ollama + nomic-embed-text + Chroma, one script per step

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