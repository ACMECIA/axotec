from gps import *
import math

gps = GPS()

while True:
    # gps.print_test()

    # To watch positions
    gps.run()
    lat, long, alt = gps.get_pos()
    if lat is not None:
        print(f"Latitud: {math.round(lat,5)}; Longitud: {math.round(long,5)}; Altitud: {math.round(alt,5)}")