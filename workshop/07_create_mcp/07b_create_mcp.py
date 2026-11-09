import logging

from fastmcp import FastMCP
from fastmcp.server.middleware.logging import LoggingMiddleware

logging.basicConfig(level=logging.INFO)

mcp = FastMCP("weather")
mcp.add_middleware(LoggingMiddleware(include_payloads=True))


# name, type hints and docstring become the tool description the LLM sees
@mcp.tool
def get_temperature(city: str) -> float:
    """Get the current air temperature in °C for a city."""
    # IMPL: return the current temperature, e.g. using weather_api.get_temperature
    raise NotImplementedError


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
