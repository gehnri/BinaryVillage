import sys 
import signal


class SysCleaner:

    def __init__(self):
        self.cleanListenerList=[]
        signal.signal(signal.SIGINT, self.OnSysEx)

    def addCleanListener(self, listener):
        self.cleanListenerList.append(listener)

    def OnSysEx(self,s,ha):
        for l in  self.cleanListenerList:
            l.Clean()
        print ("BYE BYE")
        sys.exit(0)
        