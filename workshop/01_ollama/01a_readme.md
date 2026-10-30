# Ollama

## 1. Install

[Install Ollama](https://ollama.com/download) on your device

## 2. Pull a model

Go to [Ollama Model Search](https://ollama.com/search). Search for a model and pick one that runs
on your hardware and ideally has: *Tools*, *Thinking* and *Vision*. Also decide on the *quantization*.

- For GPU, "Download Size" should ideally not be more than ~80% of your GPU RAM
  - For example *gemma4:e4b* or *qwen3.5:4b*
- For CPU, pick a small model (probably has not tool, thinking and vision but that is fine for the moment)
  - For example *gemma3:1b*

Pull the model `ollama run <model_id>`

## 3. Run some basic test

Run it and explor it: `ollama run <model_id>`

Some useful commands:

- `/bye`: to exit while running a model
- `/?`: show all command while running a model
- `ollama run --verbose <model_id>`: Show token usage and speed
- `ollama list`: Show all models

You can also explore the [Quickstart](https://docs.ollama.com/quickstart) on your own
