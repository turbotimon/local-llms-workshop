"""01 – Call a local model with Pydantic AI. Run: uv run workshop/02_sdk/app_01.py"""

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

BASE_URL = "http://localhost:1234/v1"

# IMPL set your model here
MODEL_NAME = ""

provider = OpenAIProvider(base_url=BASE_URL, api_key="<not needed>")

model = OpenAIChatModel(MODEL_NAME, provider=provider)

agent = Agent(model)

result = agent.run_sync("You are MC LMM, only answer in sweet rap rhymes (max. 5 bars): What time is it?")
print(f"*** OUTPUT ***")
print(result.output["message"]["content"])
