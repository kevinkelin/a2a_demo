#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   agent_hello.py
@Time    :   2025/05/18 18:32:44
@Author  :   YangYanxing 
@Desc    :   None
'''
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def say_hello(name: str = "there") -> str:
    """提供以个友好的问候语，可选的 name 参数

    Args:
        name (str, optional): 需要问候的人名称. 默认值 "there".

    Returns:
        str: 一个友好的问候语.
    """
    return f"Hello, {name}!"

def say_goodbye() -> str:
    """提供一个简单的告别信息，以结束对话。"""
    return "Goodbye! Have a great day."

MODEL_QWEN = "openai/qwen-plus"

greetting_agent = Agent(
    name="greetting_agent",
    model=LiteLlm(model=MODEL_QWEN),
    description=(
        "问候和告别的agent."
    ),
    instruction=(
        "你是一个问候和告别的agent，你的工作只有两个任务，"
        "1. 你可以使用 say_hello 函数给用户一个友好的问候，并返回一个友好的问候语,如果用户提供了name，则需要传递到函数中"
        "2. 你可以给用say_goodbye 函数给用户一个友好的告别，并返回一个友好的告别信息。"
    ),
    tools=[say_hello, say_goodbye]
)