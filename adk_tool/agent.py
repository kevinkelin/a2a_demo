from google.adk.agents import Agent

from adk_tool.agent_tool import get_weather, get_current_time
from google.adk.tools import google_search,built_in_code_execution,VertexAiSearchTool
from google.adk.models.lite_llm import LiteLlm

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


MODEL_QWEN = "openai/qwen-plus"

root_agent = Agent(
    name="weather_time_agent",
    model=LiteLlm(model=MODEL_QWEN),
    description=(
        "获取天气和google搜索的agent."
    ),
    instruction=(
        "你是一个非常有用的助手，可以获取天气和当前的时间信息"
        "当询问天气信息时，请使用get_weather函数，当获取时间信息时，请使用get_current_time函数。"
        "其他你不知道的内容你可以使用google搜索来获取信息，但是不要使用google搜索来获取天气信息。"
    ),
    tools=[get_weather, get_current_time, google_search] 
)