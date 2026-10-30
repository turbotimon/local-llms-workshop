# 03 – Agent harnesses (OpenCode)

An agent harness wraps a model with tools such as reading and writing files and running commands. In this part you run OpenCode with a local model.

## 1. Install OpenCode

Docs: https://opencode.ai/docs

```bash
curl -fsSL https://opencode.ai/install | bash
# or: npm install -g opencode-ai
```

IMPL: Install OpenCode and check that `opencode` starts.

## 2. Configure a local provider

Put the config in one of these places:

- Project: `opencode.json` in the folder where you start OpenCode (here `workshop/03_harnesses/opencode.json`)
- Global: `~/.config/opencode/opencode.json`

OpenCode merges both files. If a key is set in both, the project file wins.

Minimal `opencode.json` with both local providers. Keep the one you use:

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
        "gemma4:e4b": {
          "name": "Gemma 4 e4b (Ollama)"
        }
      }
    },
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        "baseURL": "http://localhost:1234/v1"
      },
      "models": {
        "<your-model-id>": {
          "name": "My LM Studio model"
        }
      }
    }
  },
  "model": "ollama/gemma4:e4b"
}
```

- `model`: default model in the format `provider-id/model-id`. You can also switch models in the TUI with `/models`.
- LM Studio: replace `<your-model-id>` with the id shown by `curl http://localhost:1234/v1/models`.
- Ollama: if tool calls don't work, increase `num_ctx` in Ollama. The docs suggest starting with 16k to 32k.
- Optional: use `"permission": { "edit": "ask", "bash": "ask" }` to make OpenCode ask before it edits files or runs commands.

IMPL: Create `opencode.json` for your provider and model.

## 3. Let the agent write code

```bash
cd workshop/03_harnesses
opencode
```

IMPL: Paste a prompt like this one:

```text
Write a Python script weather.py with a function
get_temperature(city: str) -> float that returns the current temperature in °C
for a city using the Open-Meteo API (https://open-meteo.com/en/docs).
First get the coordinates of the city with the geocoding API
(https://open-meteo.com/en/docs/geocoding-api).
Use the requests library. Add a __main__ block that prints the temperature for "Zurich".
```

Hints:

- Getting the coordinates of a city is a separate step. Use the geocoding API: https://open-meteo.com/en/docs/geocoding-api
- `requests` is already in the root `pyproject.toml`. If it is missing, run `uv add requests`.

## 4. Run it

```bash
uv sync          # once, at repo root
uv run weather.py
```

IMPL: Run the script. If it fails, give the error to the agent and let it fix the script.
