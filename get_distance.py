import geopy.distance


def calculate_dist(coords_1_lat, coords_1_lon, coords_2_lat, coords_2_lon):
    coords_1 = (52.2296756, 21.0122287) # lat and lon of the ISS
    coords_2 = (46.5009293,-80.9997138) # my location is 341 mabel avenue

    return geopy.distance.geodesic(coords_1, coords_2).km
    #return from the distance