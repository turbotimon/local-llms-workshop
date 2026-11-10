"""04 – Solution: send a picture to the model. Run: uv run workshop/02_sdk/app04_SOLUTION.py"""

from datetime import datetime
from pathlib import Path

from pydantic_ai import Agent, BinaryContent, ModelSettings
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

IMAGE = Path(__file__).parent.parent / "02_api" / "bern.jpg"

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

# a prompt can be a list of text and media parts
result = agent.run_sync([
    "Which city is shown in the image?",
    BinaryContent(data=IMAGE.read_bytes(), media_type="image/jpeg"),
])
print(result.output)
