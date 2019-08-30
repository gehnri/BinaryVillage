import json

class SaveIdToJson:

    def __init__(self,cInputManager,filePath="Assets/loggedIds.json"):
        self.filePath=filePath
        self.cInputManager=cInputManager
        self.startOfValChar=">"
        self.endOfValChar="<"
        self.endOfline=";"
    
    
    def loggFilePath(self,nfcId,cInputManager):
        self.nfcId=nfcId
        cInputManager.getStringVal(self,"What soundfile is this id "+ nfcId + " \n \t Enter only filename + format (sound.wav): \n \t ")
        
    def callback(self,val):
        soundFileName=val
        print "\n Saving: " + soundFileName + " on id:  "+ self.nfcId + " to file: "+ self.filePath
        import json

        audioIdOut  = {self.nfcId:soundFileName}

        with open(self.filePath) as f:
            data = json.load(f)

        data.update(audioIdOut)

        with open(self.filePath, 'w') as f:
            json.dump(data, f)
        
    def recievedMessage(self,msg):
        self.processMessage(msg)

    def processMessage(self,msg):
        # channel:>channelNumber<; songId:>0xz212<;
            if "channel" in msg:
                startOfValStringIndex=msg.find("channel")
                endOfIndex=msg.find(self.endOfline)
                self.channel=self.getValueFromString(msg[startOfValStringIndex:endOfIndex])
            
            if "songId" in msg:
                startOfValStringIndex=msg.find("songId")
                self.songId=self.getValueFromString(msg[startOfValStringIndex:])
            
            self.loggFilePath(self.songId,self.cInputManager)

    def getValueFromString(self, msg):
        startInd=msg.find(self.startOfValChar)
        endInd=msg.find(self.endOfValChar)
        if startInd !=-1 and endInd !=-1:
                val=msg[startInd+1:endInd]
                return val
        return " "    