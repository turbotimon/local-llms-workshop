"""01 – Call a local model with Pydantic AI. Run: uv run workshop/02_sdk/app_01.py"""

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

# LM Studio server (Developer tab -> Start Server); local, so any api_key works
provider = OpenAIProvider(base_url="http://localhost:1234/v1", api_key="lm-studio")
# model id as listed by: curl http://localhost:1234/v1/models
model = OpenAIChatModel("google/gemma-4-e4b", provider=provider)

agent = Agent(model)

result = agent.run_sync("You are MC LMM, only answer in sweet rap rhymes: What time is it?")
print(result.output)
