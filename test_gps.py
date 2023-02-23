from gps import *

gps = GPS()

while True:
    
    vel_gps = gps.get_vel()
    if gps.get_vel() is not None:
        print(gps.get_vel())