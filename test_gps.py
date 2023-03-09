from gps import *

gps = GPS()

while True:

    lat, long, alt = gps.get_pos()
    if lat is not None:
        print(f"Latitud: {lat}; Longitud: {long}; Altitud: {alt}")