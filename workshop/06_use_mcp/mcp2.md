# 04b – Use a local MCP (fetch)

A local MCP server runs as a process on your machine. Example: the fetch server
https://github.com/modelcontextprotocol/servers/tree/main/src/fetch

It provides a `fetch` tool that loads a URL and returns its content as Markdown.

## 1. Try the server

Using `uvx`, no install needed:

```bash
uvx mcp-server-fetch
```

The server waits for input on stdin. Stop it with `Ctrl+C`. OpenCode starts it for you later.

Alternative with Docker: `docker run -i --rm mcp/fetch`

## 2. Add it to OpenCode

Add this to your `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "fetch": {
      "type": "local",
      "command": ["uvx", "mcp-server-fetch"],
      "enabled": true
    }
  }
}
```

IMPL: Add the snippet and start `opencode` again.

## 3. Use it

IMPL: Ask the agent:

```text
use the fetch tool to fetch https://ollama.com/blog and summarize the latest posts
```

IMPL: Check that the agent calls the `fetch` tool and does not answer from memory.
