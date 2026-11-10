# Solution

## 1. Basics

```sh
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.5:9b",
    "messages": [
      {"role": "user", "content": "What is the capital of Switzerland?"}
    ]
  }'
```

## 2. Thinking

```sh
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.5:9b",
    "thinking": {"type": "enabled"},
    "messages": [
      {"role": "user", "content": "Why do some people think the capital of Switzerland is Zurich?"}
    ]
  }'
```

## 3. Structured output

```sh
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.5:9b",
    "messages": [
      {"role": "user", "content": "List the 5 biggest cities of switzerland"}
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "cities",
        "schema": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "city": {"type": "string"},
              "canton": {"type": "string"},
              "population": {"type": "integer"}
            },
            "required": ["city", "canton", "population"]
          }
        }
      }
    }
  }'
```

## 4. Optional: Multimodal Input / Vision

```sh
IMG="data:image/jpeg;base64,$(base64 -w0 bern.jpg)"
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"qwen3.5:9b\",
    \"messages\": [
      {\"role\": \"user\", \"content\": [
        {\"type\": \"text\", \"text\": \"Which city is shown in the image?\"},
        {\"type\": \"image_url\", \"image_url\": {\"url\": \"$IMG\"}}
      ]}
    ]
  }"
```
