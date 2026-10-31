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

Run it the model and chat with it: `ollama run <model_id>`

Some useful commands:

- `/bye`: to exit while running a model
- `/?`: show all command while running a model
- `ollama run --verbose <model_id>`: Show token usage and speed
- `ollama run <model_id> "What is the capital of Switzerland?"`: Run a model non-interactively
- `ollama list`: Show all models

## (4. Optional)

- Explore the [Quickstart](https://docs.ollama.com/quickstart)
- Explore the full [CLI](https://docs.ollama.com/cli)
- Try out a [Decicion Model](https://docs.ollama.com/capabilities/decision)*

\* A decision model is a special model can only answer one of these question types. The benefit is, it can do so in just one-forward pass (just one token to create) and therefore is faster than generating a full answer:
- Yes/No
- Choose from predefined list
- Score on a predefined score
