from ValueMapper import ValueMapper
class RotaryConverter(ValueMapper,object):

    def __init__(self, inputMax,inputMin):
        self.inputMax=inputMax
        self.inputMin=inputMin
        super(ValueMapper,self).__init__()

    def convertStepInDegrees(self, inputVal):
        #max und min values aus der prefs datei beziehen
        convertedVal= self.mapValues(inputVal,self.inputMax,self.inputMin,210.0,0.0)
        return convertedVal

    