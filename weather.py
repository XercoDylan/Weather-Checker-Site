from dotenv import load_dotenv
from pprint import pprint
import requests
import os
from pathlib import Path

env_path = Path("/etc/secrets/.env")
load_dotenv(dotenv_path=env_path)


def get_current_weather(city="Upper Marlboro"):
    print(os.getenv("API_KEY"), flush=True )
    requests_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(requests_url).json()
    return weather_data
