class GetIDViaOsc:

    def __init__(self,idChecker,oscSoundSender,oscSoundDict):
        pass
        self.idChecker=idChecker
        self.oscSoundSender=oscSoundSender
        self.oscSoundDict=oscSoundDict
        self.startOfValChar=">"
        self.endOfValChar="<"
        self.endOfline=";"

    def recievedMessage(self, msg):
        # id wert nummer des channels 
        # id = sdfs; channel=0;
        self.songId=-1
        self.channel=-1

        self.processMessage(msg)
        if self.idChecker.checkForId(self.songId):
            self.oscSoundSender.sendIDWithSound(self.channel,self.oscSoundDict[self.songId])
        else :
            print "Couldnt find id "+ self.songId + " file: "+self.channel

    def processMessage(self,msg):
        # channel:>channelNumber<; songId:>0xz212<;
            if "channel" in msg:
                startOfValStringIndex=msg.find("channel")
                endOfIndex=msg.find(self.endOfline)
                self.channel=self.getValueFromString(msg[startOfValStringIndex:endOfIndex])
            
            if "songId" in msg:
                startOfValStringIndex=msg.find("songId")
                self.songId=self.getValueFromString(msg[startOfValStringIndex:])

    def getValueFromString(self, msg):
        startInd=msg.find(self.startOfValChar)
        endInd=msg.find(self.endOfValChar)
        if startInd !=-1 and endInd !=-1:
                val=msg[startInd+1:endInd]
                return val
        return " "    