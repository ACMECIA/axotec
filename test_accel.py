from accelerometer import Accelerometer

def main():
    accel = Accelerometer()
    
    # Calibration (Al calibrar, la frecuencia se actualiza)
    accel.calibrate()
    accel.getSamplingFreq()
    while True:
        accel.printAccel()
        #print(accel.getSpeed())
        #thx,thy =accel.getAngles()
        #print(thx, thy)

main()