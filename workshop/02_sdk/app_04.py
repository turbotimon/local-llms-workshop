"""04 (optional) – Images: send a picture to the model. Run: uv run workshop/02_sdk/app_04.py"""

from datetime import datetime

from pydantic_ai import Agent, ModelSettings
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

provider = OpenAIProvider(base_url="http://localhost:1234/v1", api_key="lm-studio")
model = OpenAIChatModel("google/gemma-4-e4b", provider=provider)  # needs a vision model

agent = Agent(
    model,
    instructions="You are MC LMM, only answer in sweet rap rhymes.",
    model_settings=ModelSettings(temperature=0.8, top_p=0.9, thinking="low", max_tokens=1000, seed=42),
)


@agent.tool_plain
def get_time() -> str:
    """Return the current local time."""
    return datetime.now().strftime("%H:%M")


result = agent.run_sync("What time is it?")
print(result.output)

# IMPL: send ../01_api/bern.jpg with the question "Which city is shown in the image?"
#       find out yourself how: https://ai.pydantic.dev/input/
