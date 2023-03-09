from gps import *

gps = GPS()

while True:
    gps.run()
    lat, long, alt = gps.get_pos()
    print(f"Latitud: {lat}; Longitud: {long}; Altitud: {alt}")