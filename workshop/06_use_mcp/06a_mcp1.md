# 06a – Use a remote MCP (Context7)

In this part we will see how to use a remote MCP server and include it in our OpenCode config. 

We will use Context7 as an example. Context7 is a remote MCP server. It gives the agent up-to-date library docs.

We will use the MCPs in OpenCode, but you could also include it in LM Studio, Ollama or use it in your own code with an SDK.

## 1. Get an API key

- Create an account at https://context7.com and create an API key in the dashboard.
- Export the key as an environment variable:

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

Add the snippet and start `opencode` again.

## 3. Check and use it

```bash
opencode mcp list
```

Ask the agent:

```text
use context7 to look up how to define a tool in FastMCP
```

Check whether the agent really calls the Context7 tools (`resolve-library-id`, `query-docs`).
