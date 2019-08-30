import json
class DispatcherPrefReader:

    def __init__(self,filePath="Assets/messageDispatcherPrefs.json"):

        self.filePath=filePath

    def getSleepTimeOut(self):
        #sleepTime
        with open(self.filePath) as json_file:
            data = json.load(json_file)
            return data["timeOut"] 
    
    def getSerialTimeOut(self):
        with open(self.filePath) as json_file:
            data = json.load(json_file)
            return data["serialTimeOut"] 