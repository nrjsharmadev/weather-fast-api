import aiohttp
import asyncio
from fastapi import FastAPI
from utils import (get_city_local_time, get_city_weather)

app = FastAPI()


@app.get('/current-datetimes')
async def get_current_datetimes(city1: str, city2: str):
    """
    API takes two string parameter city1 and city2
    and return current date and time of given cites
    :param city1:
    :param city2:
    :return: Current date and time of city
    """
    return_data = []
    async with aiohttp.ClientSession() as session:
        datas = await asyncio.gather(*[get_city_local_time(session, city) for city in [city1, city2]])
        for data in datas:
            return_data.append(
                {data['data']['request'][0]['query'].title(): data['data']['time_zone'][0]['localtime']}
            )
        return return_data


@app.get('/current-datetimes-temp')
async def get_current_datetimes_temp(city1: str, city2: str):
    """
    API takes two string parameter city1 and city2
    and return current date and temperature of given cites
    :param city1:
    :param city2:
    :return: Current date and temperature of city
    """
    return_data = []
    async with aiohttp.ClientSession() as session:
        datas = await asyncio.gather(*[get_city_weather(session, city) for city in [city1, city2]])
        for data in datas:
            return_data.append(
                {data['data']['request'][0]['query'].title(): f"{data['data']['current_condition'][0]['temp_F']}F"}
            )
        return return_data
