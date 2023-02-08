
async def get_city_local_time(session, city):
    """
    method used to get current date and time of city
    """
    url = f"https://api.worldweatheronline.com/premium/v1/tz.ashx?q={city}&format=JSON&key=f3abda657228456396e125339230602"
    async with session.get(url) as r:
        return await r.json()


async def get_city_weather(session, city):
    """
    method used to get current date and temperature of city
    """
    url = f"https://api.worldweatheronline.com/premium/v1/weather.ashx?q={city}&key=f3abda657228456396e125339230602&format=JSON"
    async with session.get(url) as r:
        return await r.json()
