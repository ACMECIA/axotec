
from libcan import CAN
import os, time


# CAN configuration

can_frame_fmt = "=IB3x8s"

can_port = "can0"

can = CAN(can_frame_fmt, can_port)



while True:

    can_vel = can.get_vel(10)

    print(can_vel)