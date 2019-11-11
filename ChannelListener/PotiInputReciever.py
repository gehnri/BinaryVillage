import Adafruit_ADS1x15

class PotiInputReciever:

    def __init__(self):
        self.inputListenerList=[]
        self.adc = Adafruit_ADS1x15.ADS1115()

      
    def addListener(self,inputListener):
        self.inputListenerList.append(inputListener)
            
    def checkRotation(self):
       val=self.adc.read_adc(0, gain=1)
       self.informListenerOnRotation(val)

    def informListenerOnRotation(self,val):
       for l in self.inputListenerList:
           l.onRotate(val)