import urllib.request
import json


def weather_info(lat,lon):
    key = '8238b79383d6e17d4f570a3c5c1ba512'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    return result

