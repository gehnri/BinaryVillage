from ValueMapper import ValueMapper
class AngleToVolumeConverter(ValueMapper,object):

    def __init__(self, inputMax,inputMin):
        super(ValueMapper,self).__init__()
        self.inputMax=inputMax
        self.inputMin=inputMin

    def convertAngleIntoVolume(self, inputVal):
        convertedVal= self.mapValues(inputVal,self.inputMax,self.inputMin,100,0)
        finalVal=convertedVal/100
        return finalVal

    