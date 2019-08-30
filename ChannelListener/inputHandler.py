import Adafruit_ADS1x15

class ArduinoInputHandler:

    def __init__(self):
        self.rotaryListener=[]
        self.adc = Adafruit_ADS1x15.ADS1115()

      
    def addListener(self,rotaryListener):
        self.rotaryListener.append(rotaryListener)
            
    def checkRotation(self):
       val=self.adc.read_adc(0, gain=1)
       self.informListenerOnRotation(val)

    def informListenerOnRotation(self,val):
       for l in self.rotaryListener:
           l.onRotate(val)