from ValueMapper import ValueMapper

class AngleConverter(ValueMapper,object):

    def __init__(self, inputMax,inputMin):
        self.inputMax=inputMax
        self.inputMin=inputMin
        super(ValueMapper,self).__init__()

    def convertStepInAngle(self, inputVal):
        #Only converts angles from 210 to 0 because of the potentiometer
        convertedVal= self.mapValues(inputVal,self.inputMax,self.inputMin,210.0,0.0)
        return convertedVal

    