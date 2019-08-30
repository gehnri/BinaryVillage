from ValueMapper import ValueMapper
class RotaryConverter(ValueMapper,object):

    def __init__(self, inputMax,inputMin):
        self.inputMax=inputMax
        self.inputMin=inputMin
        super(ValueMapper,self).__init__()

    def convertStepInDegrees(self, inputVal):
        convertedVal= self.mapValues(inputVal,self.inputMax,self.inputMin,210.0,0.0)
        return convertedVal

    