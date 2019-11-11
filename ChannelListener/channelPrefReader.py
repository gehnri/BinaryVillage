import json
class ChannelPrefReader:

    def __init__(self,filePath="Assets/channelPrefs.json"):

        self.filePath=filePath

    
    def getAngleOf(self,identifier):
        with open(self.filePath) as json_file:
            data = json.load(json_file)
            angleObject=data["channelAngle"]
            angleArray=angleObject[identifier]
            angle=(angleArray[0],angleArray[1],angleArray[2])
        return angle
    
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