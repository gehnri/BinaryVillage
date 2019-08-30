import OSC
import threading
import socket

class OSCInputHandler:

    def __init__(self,):
        self.oscListenerList=[]

    def registerCallBackListener(self,listener):
        self.oscListenerList.append(listener)
    
    def initServer(self,ipChooser):
        self.adress=ipChooser.getIpAdress()
        try:
            reciverAd=self.adress, 9000
            s = OSC.OSCServer(reciverAd)  # basic
            s.addDefaultHandlers()
            s.addMsgHandler("/binaryVillage", self.OnOSCMessage)  # adding our function
            st = threading.Thread(target=s.serve_forever)
            st.start()
        except:
            print "OSC couldnt be initet"
            self.initServer(ipChooser)


    def OnOSCMessage(self,ddr, tags, stuff, source):
        print stuff
        actionToTake=stuff[0]
        for l in self.oscListenerList:
            l.recievedMessage(actionToTake)
    
   