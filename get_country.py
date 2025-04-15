import urllib.request
import json


def country(country_code):
    CC = country_code
    url = f'https://restcountries.com/v3.1/alpha/{CC}'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    return result

