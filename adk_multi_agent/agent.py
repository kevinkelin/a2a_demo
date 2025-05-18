from google.adk.agents import Agent

from adk_multi_agent.agent_tool import weather_agent
from adk_multi_agent.agent_time import date_agent
from adk_multi_agent.agent_hello import greetting_agent
from adk_multi_agent.agent_hello import say_hello, say_goodbye
from google.adk.models.lite_llm import LiteLlm


MODEL_QWEN = "openai/qwen-plus"

root_agent = Agent(
    name="weather_time_hello_agent",
    model=LiteLlm(model=MODEL_QWEN),
    # description=(
    #     "获取天气和时间和打招呼的agent."
    # ),
    # instruction=(
    #     "你是一个非常有用的助手，可以获取天气和当前的时间信息。"
    #     "当用户向你问好是，"
    # ),
    description=(
        "你是一个协调员代理，根据用户的对话提问，并调用其他代理进行任务。"
    ),
    instruction=(
        "你是一个非常有用的助手，可以获取天气和当前的时间信息。"
        "如果用户向你打招呼或者回复了再见，你可以调用greeting_agent 进行回复。"
    ),
    sub_agents=[weather_agent, date_agent, greetting_agent]
)