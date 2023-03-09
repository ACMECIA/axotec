import serial

knots2kmh = 1.852
knots2ms = 0.514
kmh2ms = 5/18

class GPS():
    def __init__(self,port="/dev/ttyUSB1"):
        self.ser = serial.Serial(port)
        self.previous_speed = 0
        self.speed = 0
        
 
    def get_vel(self):
        try:
            received_data= (self.ser.readline()) 
            GPVTG_Data = received_data.find(b"$GPVTG,")
            if (GPVTG_Data==0):
                speed_raw = received_data.split(b",")[7]       
                self.speed = float(speed_raw)
                return self.speed
        except:
            return None
        #self.previous_speed = self.speed
        #return self.previous_speed

        
