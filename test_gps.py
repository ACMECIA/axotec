from gps import *

gps = GPS()

while True:
    # gps.print_test()

    # To watch positions
    gps.run()
    lat, long, alt = gps.get_pos()
    if lat is not None:
        print(f"Latitud: {round(lat,5)}; Longitud: {round(long,5)}; Altitud: {round(alt,5)}")