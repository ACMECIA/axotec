from accelerometer import Accelerometer

def main():
    accel = Accelerometer()
    
    # Calibration (Al calibrar, la frecuencia se actualiza)
    #accel.calibrate()
    accel.getSamplingFreq()
    while True:
        print(accel.getSpeed())

main()