class SoundMessageHandler:
    def __init__(self,audioHandler):
        self.audioHandler=audioHandler
        self.startOfValChar=">"
        self.endOfValChar="<"
        self.endOfline=";"
        
    def recievedMessage(self,msg):
        #msg templeta: action:changeSound channel:>channelNumber<; file:>filename.wav<;
        if "changeSound" in msg:
            if "channel" in msg:
                startOfValStringIndex=msg.find("channel")
                endOfIndex=msg.find(self.endOfline)
                channelVal=self.getValueFromString(msg[startOfValStringIndex:endOfIndex])
            
            if "file" in msg:
                startOfValStringIndex=msg.find("file")
                fileVal=self.getValueFromString(msg[startOfValStringIndex:])
            self.audioHandler.changeAudioFileOnChannel(channelVal,fileVal)

    def getValueFromString(self, msg):
        startInd=msg.find(self.startOfValChar)
        endInd=msg.find(self.endOfValChar)
        if startInd !=-1 and endInd !=-1:
                val=msg[startInd+1:endInd]
                return val
        return " "