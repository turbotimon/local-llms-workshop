# SDK

In this exercise, we will use the `pydantic-ai` SDK to interact with a local LLM server.

These SDKs are more convenient than using the raw API and provide lots of useful features.

## Provider

The exercises are configured to use LLM Studio as the provider. But you can also change it to Ollama or, if you have problems running decent models on your local machine, use the OST LLM Hub:

```py
BASE_URL = "https://api.llmhub.infs.ai/v1"
MODEL_NAME = "Qwen3.8-27B"
API_KEY = "<ask your instructor>
```

## Exercises

Go through the examples. Make sure you understand the code. Parts where you need to do something are marked with `# IMPL`.

