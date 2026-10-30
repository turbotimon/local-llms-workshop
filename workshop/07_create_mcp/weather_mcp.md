# 05 – Create your own MCP

- FastMCP: https://gofastmcp.com
- Model Context Protocol: https://github.com/modelcontextprotocol

## 1. Implement the tool

IMPL: Fill in `get_temperature` in [server.py](server.py) (solution idea: [weather_api.py](weather_api.py)).

## 2. Run the server

```bash
uv run workshop/05_create_mcp/server.py
```

The MCP endpoint is `http://127.0.0.1:8000/mcp`. Keep the terminal open to see the log.

## 3. Connect a client

IMPL: Add the server to LM Studio: "Program" tab in the right sidebar → `Install > Edit mcp.json`:

```json
{
  "mcpServers": {
    "weather": {
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

Docs: https://lmstudio.ai/docs/app/mcp

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

## 4. Try it out

IMPL: Ask the model:

> Do you think it is good weather to go for a swim in lake zurich near Rapperswil?

Watch the server log to see the `tools/call` of `get_temperature` and its arguments.
