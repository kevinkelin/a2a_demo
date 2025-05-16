from google.adk.agents import Agent

from adk_starter.agent_tool import get_weather, get_current_time
from google.adk.models.lite_llm import LiteLlm




MODEL_QWEN = "openai/qwen-plus"

root_agent = Agent(
    name="weather_time_agent",
    model=LiteLlm(model=MODEL_QWEN),
    description=(
        "获取天气和时间的agent."
    ),
    instruction=(
        "你是一个非常有用的助手，可以获取天气和当前的时间信息。"
    ),
    tools=[get_weather, get_current_time]
)