# -*- coding: utf-8 -*-
"""
 @Time    : 2025-05-16 11:29
 @Author  : YangYanxing
 @File    : agent_tool.py
 @Description : agent 用到的tool 定义
"""

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

async def get_weather(city: str)-> dict:
    """获取天气
    Args:
        city (str): 要查询天气的城市名称, 例如：北京.

    Returns:
        dict: 该城市的天气信息 或者  错误信息.
    
    """
    weather_data = WeatherInfo()
    api_key = os.getenv("GAODE_KEY", "")
    if not api_key:
        weather_data.status = "error"
        weather_data.message = "未配置高德地图API Key"
        return weather_data.model_dump()
    api_domain = 'https://restapi.amap.com/v3'
    url = f"{api_domain}/config/district?keywords={city}"f"&subdistrict=0&extensions=base&key={api_key}"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    async with httpx.AsyncClient(headers=headers, verify=False) as client:
        response = await client.get(url)
        if response.status_code != 200:
            weather_data.status = "error"
            weather_data.message = "查询失败"
            return weather_data.model_dump()
        
        city_info = response.json()
        if city_info["info"] != "OK":
            weather_data.status = "error"
            weather_data.message = "获取城市信息查询失败"
            return weather_data.model_dump()
        CityCode = city_info['districts'][0]['adcode']
        weather_url = f"{api_domain}/weather/weatherInfo?city={CityCode}&extensions=all&key={api_key}"
        weatherInfo_response = await client.get(weather_url)
        if weatherInfo_response.status_code != 200:
            weather_data.message = "查询天气信息失败"
            weather_data.status = "error"
            return weather_data.model_dump()
        weatherInfo = weatherInfo_response.json()
        if weatherInfo['info'] != "OK":
            weather_data.message = "查询天气信息失败"
            weather_data.status = "error"
            return weather_data.model_dump()
        weatherInfo_data = weatherInfo_response.json()
        contents = []
        if len(weatherInfo_data.get('forecasts')) <= 0:
            weather_data.message = "没有获取到该城市的天气信息"
            weather_data.status = "error"
            return weather_data.model_dump()
        for item in weatherInfo_data['forecasts'][0]['casts']:
            content = {
                'date': item.get('date'),
                'week': item.get('week'),
                'dayweather': item.get('dayweather'),
                'daytemp_float': item.get('daytemp_float'),
                'daywind': item.get('daywind'),
                'nightweather': item.get('nightweather'),
                'nighttemp_float': item.get('nighttemp_float')
            }
            contents.append(content)
        weather_data.data = contents
        weather_data.status = "success"
        weather_data.message = "获取天气成功"
        return weather_data.model_dump()
    

async def get_current_time() -> str:
    """
    获取当前时间
    Returns:
        str: 当前的时间.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    