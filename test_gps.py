from gps import *

gps = GPS()

while True:
    # gps.print_test()

    gps.run()
    lat, long, alt = gps.get_pos()
    if lat is not None:
        print(f"Latitud: {lat}; Longitud: {long}; Altitud: {alt}")