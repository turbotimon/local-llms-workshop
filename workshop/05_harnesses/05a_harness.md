# 05 – Agent harnesses (OpenCode)

An agent harness wraps a model with tools such as reading and writing files and running commands.

There are many agent harnesses available. In this part we will use OpenCode as an example.

## 1. Install OpenCode

Docs: https://opencode.ai/docs

```bash
curl -fsSL https://opencode.ai/install | bash
# or: npm install -g opencode-ai
```

IMPL: Install OpenCode and check that `opencode` starts.

## 2. Configure a local provider

Put the config in one of these places:

- Project: `opencode.jsonc`* in the folder where you start OpenCode (here `workshop/05_harnesses/opencode.jsonc`)
- Global: `~/.config/opencode/opencode.json`

\* `jsonc` is JSON with comments, but a regular `json` file works too.

OpenCode merges both files, the project file wins.

Minimal `opencode.jsonc` with both local providers. Adopt it to your needs and save it:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        // IMPL replace with your model-id and give it a name of your choice
        "<model-id>": {
          "name": "<name>"
        }
      }
    },
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        "baseURL": "http://localhost:1234/v1"
      },
      // IMPL replace with your model-id and give it a name of your choice
      "models": {
        "<your-model-id>": {
          "name": "<name>"
        }
      }
    }
  },
  // set a default model (optional)
  //"model": "<default model>"
}
```

- `model`: default model in the format `provider-id/model-id`. You can also switch models in the TUI with `/models`.
- Optional: use `"permission": { "edit": "ask", "bash": "ask" }` to make OpenCode ask before it edits files or runs commands.

## 3. Let the agent write code

```bash
cd workshop/05_harnesses
opencode
```

- Check if your models are avilable with `/models`. If not, check your `opencode.json` and the model id.

- Paste a prompt like this one:

```text
Write a Python script weather.py with a function
get_temperature(city: str) -> float that returns the current temperature in °C
for a city using the Open-Meteo API (https://open-meteo.com/en/docs).
First get the coordinates of the city with the geocoding API
(https://open-meteo.com/en/docs/geocoding-api).
Use the requests library. Add a __main__ block that prints the temperature for "Zurich".
Use pyproject.toml and uv at the root fo this repo.
```

Hints:

- Getting the coordinates of a city is a separate step. Use the geocoding API: https://open-meteo.com/en/docs/geocoding-api
- `requests` is already in the root `pyproject.toml`. If it is missing, run `uv add requests`.
- The open-code harness predefined a long system prompt, this means:
  - you wait longer for the answer, as the input needs to be processed by the model first
  - you may need to increase to context length for your model if you get an error.

## 4. Run it

```bash
uv sync          # once, at repo root
uv run weather.py
```

Run the script. If it fails, give the error to the agent and let it fix the script.

## (5. Optional: Discover more)

- Discover more [configuration options](https://opencode.ai/docs/config/)
- Read about [available commands](https://opencode.ai/docs/commands/)
- Create your [own agent with his own instructions and permissions](https://opencode.ai/docs/agents/)
- Use [skills](https://opencode.ai/docs/skills/)
