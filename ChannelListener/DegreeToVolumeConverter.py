from ValueMapper import ValueMapper
class DegreeToVolumeConverter(ValueMapper,object):

    def __init__(self, inputMax,inputMin):
        super(ValueMapper,self).__init__()
        self.inputMax=inputMax
        self.inputMin=inputMin

    def convertDegreesInVolume(self, inputVal):
        convertedVal= self.mapValues(inputVal,self.inputMax,self.inputMin,100,0)
        finalVal=convertedVal/100
        return finalVal

    