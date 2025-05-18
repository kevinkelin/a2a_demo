#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   agent_time.py
@Time    :   2025/05/18 18:26:28
@Author  :   YangYanxing 
@Desc    :   定义 获取时间的agent
'''
import datetime
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

async def get_current_time() -> str:
    """
    获取当前时间
    Returns:
        str: 当前的时间.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


MODEL_QWEN = "openai/qwen-plus"

date_agent = Agent(
    name="time_agent",
    model=LiteLlm(model=MODEL_QWEN),
    description=(
        "获取当前时间的agent."
    ),
    instruction=(
        "你是一个非常有用的助手，可以获取当前的时间信息。"
    ),
    tools=[get_current_time]
)