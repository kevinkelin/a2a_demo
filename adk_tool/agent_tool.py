#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   agent_tool.py
@Time    :   2025/05/17 21:29:48
@Author  :   YangYanxing 
@Desc    :   None
'''

import datetime
import httpx
import os
from pydantic import BaseModel
from typing import List, Dict, Any

class WeatherInfo(BaseModel):
    """天气信息"""
    status: str = "success"
    message: str = ""
    data: List[Dict[str, Any]]  = []

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我是{self.name}, 我今年{self.age}岁."

async def get_weather(city: str)-> dict:
    """获取天气
    Args:
        city (str): 要查询天气的城市名称, 例如：北京.

    Returns:
        dict: 该城市的天气信息 或者  错误信息.
    
    """
    return {
        "status": "error",
        "message": "",
        "data": [
            {
                "city": city,
                "temperature": 25,
                "weather": "晴天",
                "wind": "微风",
                "humidity": 60,
                "date": datetime.datetime.now().strftime("%Y-%m-%d")
            }
        ]
    }
    

async def get_current_time() -> str:
    """
    获取当前时间
    Returns:
        str: 当前的时间.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")