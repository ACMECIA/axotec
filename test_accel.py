from accelerometer import Accelerometer
import math
def main():
    accel = Accelerometer()
    
    # Calibration (Al calibrar, la frecuencia se actualiza)
    #accel.calibrate()
    accel.getSamplingFreq()
    while True:
        #accel.printAccel()
        #print(accel.getSpeed())
        thx,thy =accel.getAngles()
        print(thx*180/math.pi, thy*180/math.pi)

main()