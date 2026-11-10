# 06b – Use a local MCP (fetch)

In this part we will see how to use a local MCP server and include it in our OpenCode config.

A local MCP server runs as a process on your machine. We will use the fetch server MCP as an example: 
https://github.com/modelcontextprotocol/servers/tree/main/src/fetch

It provides a `fetch` tool that loads a URL and returns its content as Markdown.

You can find many other MCP server examples in the same repo. Most MCP are commonly instlled with `npx` or `uvx`. Do get a better isolation, you can also run them in Docker.

## 1. Try the server

Install it with `uvx`:

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

Then start start `opencode` again.

## 3. Use it

Ask the agent:

```text
fetch https://www.open-ost.ch/events/ and tell me the next upcoming event
```
