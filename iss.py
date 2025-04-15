import urllib.request
import json


def iss_loc():
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    #print(result) # this prints out everything in result
    lat = result["iss_position"]["latitude"]
    lon = result["iss_position"]["longitude"]
    print('Google Map:' f'http://maps.google.com/maps?q={lat},{lon}')
    return lat,lon