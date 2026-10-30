# 04a – Use a remote MCP (Context7)

Context7 is a remote MCP server. It gives the agent up-to-date library docs.

## 1. Get an API key

IMPL: Create an account at https://context7.com and create an API key in the dashboard.

IMPL: Export the key as an environment variable:

```bash
export CONTEXT7_API_KEY="<your-api-key>"
```

## 2. Add the MCP server to OpenCode

Add this to your `opencode.json`, next to your provider config from part 03:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "context7": {
      "type": "remote",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "{env:CONTEXT7_API_KEY}"
      }
    }
  }
}
```

- `{env:CONTEXT7_API_KEY}` is replaced with the value of the environment variable. Never put the key itself in the file and never commit it.
- The Context7 README also documents an `"Authorization": "Bearer {env:CONTEXT7_API_KEY}"` header.

IMPL: Add the snippet and start `opencode` again.

## 3. Check and use it

```bash
opencode mcp list
```

IMPL: Ask the agent:

```text
use context7 to look up how to define a tool in FastMCP
```

IMPL: Check whether the agent really calls the Context7 tools (`resolve-library-id`, `query-docs`). Then compare it with the same question without `use context7`.
