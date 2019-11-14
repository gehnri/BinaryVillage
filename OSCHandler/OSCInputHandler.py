import OSC
import threading
import socket
import signal
import sys
class OSCInputHandler:

    def __init__(self):
        self.oscListenerList=[]
        

    def registerCallBackListener(self,listener):
        self.oscListenerList.append(listener)
    
    def initServer(self,ipChooser):
        self.adress=ipChooser.getIpAdress()
        try:
            reciverAd=self.adress, 9000
            self.s = OSC.OSCServer(reciverAd)  # basic
            self.s.addDefaultHandlers()
            self.s.addMsgHandler("/binaryVillage", self.OnOSCMessage)  # adding our function
            self.st = threading.Thread(target=self.s.serve_forever)
            self.st.start()
        except :
            print "OSC couldnt be initet"
            self.initServer(ipChooser)


    def OnOSCMessage(self,ddr, tags, stuff, source):
        print stuff
        actionToTake=stuff[0]
        for l in self.oscListenerList:
            l.recievedMessage(actionToTake)

    def Clean(self):
        self.s.close()

    
   