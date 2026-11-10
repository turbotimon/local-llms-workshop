# Explore the API

To understand the API, we will make some raw curl calls. We use the [Ollama `/api`](https://docs.ollama.com/api/introduction) and the OpenAI Chat Completions endpoint: [`v1/chat/completions`](https://developers.openai.com/api/reference/resources/chat)

Also see: [OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility#%2Fv1%2Fchat%2Fcompletions)

## Chat Completion: Minimal Example

Since we are local, we do not need an API key

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

## Your Tasks

### 1. Basics

Change the above example to your model id and the following question. Explore the result:

> "What is the capital of Switzerland?"

### 2. Thinking

Look at the [documentation about thinking](https://docs.ollama.com/capabilities/thinking) to explore your models thinking capability, include these setting in your request.

For example, disable the thinking capability to get a faster response.

### 3. Structured output

We now want to force the model to answer in JSON instead of plain text. 
This would enable us to better use the anser in a application context.

See the [documentation](https://docs.ollama.com/capabilities/structured-outputs) and enable it in your request

> Force JSON output, e.g. `[{"city": ..., "canton": ..., "population": ...}]`.
> Ask the question: "List the 5 biggest cities of switzerland"

### (4. Optional: Multimodal Input / Vision)

Choose a model that supports vision capabilities. Send `bern.jpg` (in this folder) and ask "Which city is shown in the image?".

Look at the example in the [documentation](https://docs.ollama.com/capabilities/vision).

Hint: images are sent base64-encoded (`base64 -w0 bern.jpg`).


