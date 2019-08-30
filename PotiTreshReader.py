import Adafruit_ADS1x15
import time
class PotiReader:

    def __init__(self):
        self.rotaryListener=[]
        self.adc = Adafruit_ADS1x15.ADS1115()

      
    def addListener(self,rotaryListener):
        self.rotaryListener.append(rotaryListener)
            
    def checkRotation(self):
       val=self.adc.read_adc(0, gain=1)
       print val

if __name__ == '__main__':
    potiR=PotiReader()
    while True:
        potiR.checkRotation()
        time.sleep(0.1)