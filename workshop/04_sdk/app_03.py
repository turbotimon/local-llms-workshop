"""03 – Tools: let the model call a Python function. Run: uv run workshop/02_sdk/app_03.py"""

from pydantic_ai import Agent, ModelSettings
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

provider = OpenAIProvider(base_url="http://localhost:1234/v1", api_key="lm-studio")
model = OpenAIChatModel("google/gemma-4-e4b", provider=provider)

agent = Agent(
    model,
    instructions="You are MC LMM, only answer in sweet rap rhymes.",
    model_settings=ModelSettings(
        temperature=0.8,
        top_p=0.9,
        thinking="low",  # reasoning effort; True/False also works
        max_tokens=1000,
        seed=42,  # same seed + same input -> (mostly) same output
    ),
)

# IMPL: add a tool get_time() -> str that returns the current time (hint: @agent.tool_plain, datetime)
#       docs: https://ai.pydantic.dev/tools/

result = agent.run_sync("What time is it?")
print(result.output)
