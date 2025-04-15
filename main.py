from iss import iss_loc
from get_weather import weather_info
from get_address import address
from get_country import country
from get_distance import calculate_dist

#where is the iss
data = iss_loc()
lat , lon = data[0], data[1]

#this is the weather information
weather = weather_info(lat,lon)
#print(weather)

temp_c = round(weather['main']['temp']-273.15,2)
desc = weather['weather'][0]['description']


print(f'{temp_c} c, {desc}')


#address using reverse geolocation
addr = address(lat, lon)
print(f'Country Code: {addr["countryCode"]}') 

#distance between ISS and I
distance = calculate_dist(lat,lon, 46.5010604,-81.0000161)
print(f' the distance bewtween ISS and i is {distance} in km')

# getting country code
if (addr["countryCode"]== ''):
    print("The ISS is over water!!")

else:
    print(f'The ISS is over {addr['countryName']} with Country Code: {addr['countryCode']}')

    # finding country flag
    location = addr['countryCode']
    flag = country(location)[0]['flags']['png']
    print(flag)

    
