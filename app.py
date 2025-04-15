from flask import Flask, render_template, url_for
from iss import iss_loc
from get_weather import weather_info
from get_address import address
from get_country import country
from get_distance import calculate_dist



app = Flask(__name__)

@app.route('/')
def index():
    # Get ISS location
    lat, lon = iss_loc()
    
    # Get weather information
    weather = weather_info(lat, lon)
    temp_c = round(weather['main']['temp'] - 273.15, 2)
    desc = weather['weather'][0]['description']

    # Get address (reverse geolocation)
    addr = address(lat, lon)
    country_code = addr.get("countryCode", "")
    country_name = addr.get("countryName", "Unknown")

    # Calculate distance from your location
    my_lat, my_lon = 46.5010604, -81.0000161
    iss_distance = calculate_dist(lat, lon, my_lat, my_lon)

    # Check if ISS is over land or water
    if country_code == "":
        message = "The ISS is currently over water!"
        flag = None
    else:
        message = f"The ISS is over {country_name} (Country Code: {country_code})."
        flag = country(country_code)[0]['flags']['png']

    # Pass data to the HTML template
    return render_template(
        'index.html',
        lat=lat, lon=lon,
        temp=temp_c, desc=desc,
        message=message, flag=flag,
        iss_distance=iss_distance
    )

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080) 
