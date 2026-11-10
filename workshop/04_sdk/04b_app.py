"""01 – Call a local model with Pydantic AI. Run: uv run workshop/04_sdk/04b_app.py"""

from pydantic_ai import Agent
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
agent = Agent(model)

result = agent.run_sync("You are MC LMM, only answer in sweet rap rhymes (max. 5 bars): What time is it?")
print(f"*** OUTPUT ***")
print(result.output)
