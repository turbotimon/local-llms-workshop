# 05 – Create your own MCP

In this part we will create our own MCP server. It is very similar to a tool, but not tightly coupled to just on application. Instead, it runs as a separate process and can be used by multiple applications. It is also easier to reuse or share with others.

We will use [FastMCP](https://gofastmcp.com) package, which makes it very simple to create an MCP server. 

## 1. Implement the tool

Fill in `get_temperature` in [07b_create_mcp.py](07b_create_mcp.py).

## 2. Run the server

```bash
uv run workshop/05_create_mcp/server.py
```

The MCP endpoint is `http://127.0.0.1:8000/mcp`. Keep the terminal open to see the log.

## 3. Add server to LM Studio

Add the server to LM Studio: "Program" tab in the right sidebar → `Install > Edit mcp.json`:

```json
{
  "mcpServers": {
    "weather": {
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

Try it out by asking the model:

> Do you think it is good weather to go for a swim in lake zurich near Rapperswil?

Watch the server log to see the `tools/call` of `get_temperature` and its arguments.

## 4. Add server to OpenCode

Alternative: OpenCode (`opencode.json`, docs: https://opencode.ai/docs/mcp-servers):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "weather": {
      "type": "remote",
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

Try it out by asking the model:

> Do you think it is good weather to go for a swim in lake zurich near Rapperswil?

Watch the server log to see the `tools/call` of `get_temperature` and its arguments.

