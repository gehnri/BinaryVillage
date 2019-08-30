import json
class ChannelPrefReader:

    def __init__(self,filePath="Assets/channelPrefs.json"):

        self.filePath=filePath

    
    def getDegreesOf(self,identifier):
        with open(self.filePath) as json_file:
            data = json.load(json_file)
            degreeObject=data["channelDegrees"]
            degressArray=degreeObject[identifier]
            degrees=(degressArray[0],degressArray[1],degressArray[2])
        return degrees
    
    def getFirstAudioFile(self):
        #"firstAudioFile"
        with open(self.filePath) as json_file:
            data = json.load(json_file)
            return data["firstAudioFile"]
    
    def getPotiTreshold(self):
        with open(self.filePath) as json_file:
            data = json.load(json_file)
            return data["potiGrenzwerte"] #array [max, min]
    
    def getSleepTimeOut(self):
        #sleepTime
        with open(self.filePath) as json_file:
            data = json.load(json_file)
            return data["sleepTime"] 