from typing import List
from fastapi import Depends, HTTPException, Query
from apiPackages.routes import router
from apiPackages.schemas import apiSchemas

import httpx

@router.get('/weather_city', response_model=apiSchemas.weather)
def weather_city(weather: apiSchemas.weather = Depends()):
    print(weather)
    return get_weather_data(weather)

@router.get('/weather_citys', response_model=List[apiSchemas.weather])
def weather_city(country_name: str = 'IN', cities: List[str] = Query(None)):

    print(country_name)
    print(cities)
    weather_list: List[apiSchemas.weather] = []

    for city_name in cities:
        weather_list.append(get_weather_data(apiSchemas.weather(city = city_name, country_name = country_name )))

    print(weather_list)
    return weather_list

def get_weather_data(weather: apiSchemas.weather):

    apikey = '7f9e75dbfba0b07fe2e4e79fc4457342'
    url = 'http://api.openweathermap.org/data/2.5/weather?appid={}&q={},{}&units=metric'.format(apikey, weather.city, weather.country)
    with httpx.Client() as client:
        result = client.get(url)
        if result.status_code == 200:
            weather.temp = result.json()['main']['temp']
            weather.temp_min = result.json()['main']['temp_min']
            weather.temp_max = result.json()['main']['temp_max']
            weather.humidity = result.json()['main']['humidity']

            return weather
        return HTTPException(status_code=400, detail="Some error, please check if correct data is passed")