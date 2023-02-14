from accelerometer import Accelerometer

def main():
    accel = Accelerometer()
    
    # Calibration
    accel.calibrate()

    while True:
        print(accel.freq)

main()