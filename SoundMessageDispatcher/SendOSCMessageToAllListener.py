import OSC
class OSCSoundSender:
    def __init__(self, listOfListener):
        self.listOfListener=listOfListener
    
    def sendIDWithSound(self,channelId,soundFileName):
        print channelId
        print soundFileName
        msg = OSC.OSCMessage() #  we reuse the same variable msg used above overwriting it
        msg.setAddress("/binaryVillage")
        msg.append("action:changeSound channel:>"+channelId+"<; file:>"+soundFileName+"<;")
        for l in self.listOfListener:
            client = OSC.OSCClient()
            client.connect( (l, 9000) ) # note that the argument is a tupple and not two arguments
            client.send(msg)
        