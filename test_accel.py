from accelerometer import Accelerometer
import math
def main():
    accel = Accelerometer()
    
    # Calibration (Al calibrar, la frecuencia se actualiza)
    #accel.calibrate()
    #accel.getSamplingFreq()
    while True:
        #accel.printAccel()
        #print(accel.getSpeed())
        thx,thy =accel.getAngles()
        print("roll: ",thx*180/math.pi,"pitch: ", thy*180/math.pi)

main()