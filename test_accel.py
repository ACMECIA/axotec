from accelerometer import Accelerometer

def main():
    accel = Accelerometer()
    
    # Calibration
    accel.calibrate()

    while True:
        accel.printAccel()

main()