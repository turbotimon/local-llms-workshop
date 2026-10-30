"""02 – Settings: system prompt, temperature, top_p, reasoning, ... Run: uv run workshop/02_sdk/app_02.py"""

from pydantic_ai import Agent, ModelSettings
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

provider = OpenAIProvider(base_url="http://localhost:1234/v1", api_key="lm-studio")
model = OpenAIChatModel("google/gemma-4-e4b", provider=provider)

# IMPL: move "You are MC LMM, only answer in sweet rap rhymes." into a system prompt (Agent(instructions=...))
# IMPL: set model_settings=ModelSettings(...) with temperature, top_p, thinking (reasoning) and 2 more of your choice
#       docs: https://ai.pydantic.dev/agents/#model-run-settings
agent = Agent(model)

result = agent.run_sync("You are MC LMM, only answer in sweet rap rhymes: What time is it?")
print(result.output)
