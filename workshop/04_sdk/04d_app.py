"""03 – Tools: let the model call a Python function. Run: uv run workshop/04_sdk/04d_app.py"""

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

# IMPL: add a tool get_time() -> str that returns the current time
#       docs: https://ai.pydantic.dev/tools/
def get_time() -> str:
    pass

# Try it out by asking the model: "What time is it?"

print(f"Write 'exit' or 'quit' or press Ctrl+C to stop the program.")
while True:
    user_input = input(">>> ")
    if user_input.lower() in ["exit", "quit"]:
        break
    result = agent.run_sync(user_input)
    print(f"Answer: {result.output}")
