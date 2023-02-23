from gps import *

gps = GPS()

while True:

    vel_gps = gps.get_vel()
    if vel_gps is not None:
        print(vel_gps)