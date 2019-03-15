"""
Set up pyopenweatherapp
"""
import requests

API_KEY = '813ec3a13b14f61e6677112f831b877d'
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}'

def query_api(city):
    try:
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        data = None
    return data
