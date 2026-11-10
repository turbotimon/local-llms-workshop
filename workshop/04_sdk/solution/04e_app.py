"""04 – Solution: send a picture to the model. Run: uv run workshop/04_sdk/solution/04e_app_SOLUTION.py"""

from datetime import datetime
from pathlib import Path

from pydantic_ai import Agent, BinaryContent, ModelSettings
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

IMAGE = Path(__file__).parent.parent / "02_api" / "bern.jpg"

# IMPL Use http://localhost:1234/v1 for LM Studio or http://localhost:11434/v1 for Ollama
# or see 04a_sdk.md for OST LLM Hub
BASE_URL = ""

API_KEY = "<not needed for local Ollama or LM Studio>"

# IMPL set your model here (needs a vision model)
MODEL_NAME = ""

provider = OpenAIProvider(base_url=BASE_URL, api_key=API_KEY)

model = OpenAIChatModel(MODEL_NAME, provider=provider)

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
