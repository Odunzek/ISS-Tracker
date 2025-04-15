import urllib.request
import json



def address(lat, lon):
    key = 'bdc_ca78e5ffee6d4768b866d4f21e02ec69'
    url = f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={key}'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    #print(result)
    return result
