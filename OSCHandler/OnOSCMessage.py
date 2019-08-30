
class OnOSCMessage:

    def __init__(self):
        self.messageHandlerList=[]
    
    def addMessageHandler(self,messagHandler):
        self.messageHandlerList.append(messagHandler)

    def recievedMessage(self,msg):
        for handler in self.messageHandlerList:
            print handler
            handler.recievedMessage(msg)