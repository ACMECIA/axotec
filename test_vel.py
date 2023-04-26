from gps import *

gps = GPS()

while True:
    # gps.print_test()

    # To watch positions
    gps.run()
    vel = gps.get_vel()
    if vel is not None:
        print(f"Velocidad: {round(vel,2)}")