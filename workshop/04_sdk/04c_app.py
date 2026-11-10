"""02 – Settings: system prompt, temperature, top_p, reasoning, ... Run: uv run workshop/04_sdk/04c_app.py"""

from pydantic_ai import Agent, ModelSettings
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

provider = OpenAIProvider(base_url="http://localhost:1234/v1", api_key="lm-studio")
model = OpenAIChatModel("google/gemma-4-e4b", provider=provider)

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
    print(f"Answer: {result.output}")
