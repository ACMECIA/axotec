import serial

class GPS():
    def __init__(self,port="/dev/ttyUSB1"):
        self.ser = serial.Serial(port)
        self.previous_speed = 0
        self.speed = 0
        self.knots2kmh = 1.852
        self.knots2ms = 0.514
        self.kmh2ms = 5/18
 
    def get_vel(self):
        
        received_data= (self.ser.readline()) 
        GPVTG_Data = received_data.find(b"$GPVTG,")
        if (GPVTG_Data==0):
            speed_raw = received_data.split(b",")[7]       
            self.speed = float(speed_raw)*self.kmh2ms#*self.knots2ms 
            return self.speed
        self.previous_speed = self.speed
        return self.previous_speed

        
