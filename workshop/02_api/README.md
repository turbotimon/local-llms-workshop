# 01 – Raw API with curl

Ollama must be running (`ollama serve` / app). We use the OpenAI Chat Completions endpoint: http://localhost:11434/v1/chat/completions

## Example

```sh
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:31b",
    "messages": [
      {"role": "user", "content": "Say hello in one sentence."}
    ]
  }'
```

## Tasks

### 1. Pick a model

Pick a model that runs on your hardware with the capabilities reasoning (thinking), tools and vision.
Hint: gemma4 sizes e2b/e4b/12b/26b/31b (~4.6–20 GB); smaller = less RAM. Download with `ollama pull <model>`.

- https://ollama.com/search
- https://ollama.com/library/gemma4

IMPL: Change `model` to your model and ask "What is the capital of Switzerland?"

### 2. Thinking

Ask "Why do some people think the capital of Switzerland is Zurich?" and look at the model's thinking.

- https://docs.ollama.com/capabilities/thinking

IMPL: Enable thinking in the request and inspect the thinking in the response.

### 3. Structured output

Force JSON output, e.g. `{"city": ..., "canton": ..., "population": ...}`.

- https://docs.ollama.com/capabilities/structured-outputs

IMPL: Add a JSON schema / response format to the request.

### 4. Multimodal Input (Vision)

Send `bern.jpg` (in this folder) and ask "Which city is shown in the image?".
Hint: images are sent base64-encoded (`base64 -w0 bern.jpg`).

- https://docs.ollama.com/capabilities/vision

IMPL: Add the image to the message content.

---

Next: [decision.md](decision.md)
