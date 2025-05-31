import requests
from langchain_core.tools import tool

@tool
def getWeatherData(city:str)->str:
    '''Get the current weather data for a given city.'''
    url=f'http://api.weatherstack.com/current?access_key=yourapikeye&query={city}'
    response = requests.get(url)
    return response.json()


