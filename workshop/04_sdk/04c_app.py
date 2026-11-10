"""02 – Settings: system prompt, temperature, top_p, reasoning, ... Run: uv run workshop/04_sdk/04c_app.py"""

from pydantic_ai import Agent, ModelSettings
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

# IMPL Use http://localhost:1234/v1 for LM Studio or http://localhost:11434/v1 for Ollama
# or see 04a_sdk.md for OST LLM Hub
BASE_URL = ""

API_KEY = "<not needed for local Ollama or LM Studio>"

# IMPL set your model here
MODEL_NAME = ""

provider = OpenAIProvider(base_url=BASE_URL, api_key=API_KEY)
model = OpenAIChatModel(MODEL_NAME, provider=provider)

# IMPL: move "You are MC LMM, only answer in sweet rap rhymes." into a system prompt (Agent(instructions=...))
# IMPL: set model_settings=ModelSettings(...) with temperature, top_p, thinking (reasoning) and 2 more of your choice
#       docs: https://ai.pydantic.dev/agents/#model-run-settings
agent = Agent(model)

print(f"Write 'exit' or 'quit' or press Ctrl+C to stop the program.")
while True:
    user_input = input(">>> ")
    if user_input.lower() in ["exit", "quit"]:
        break
    result = agent.run_sync(user_input)
    print(result.output)
