import time
import serial
from time import sleep
import OSC
import time
import threading

class NfcSerialReader:
    def __init__(self,usbList, timeOut, serialTimeOut):
        self.listener=[]
        self.usbList=usbList
        self.timeOut=timeOut
        self.lastMessageList=["0","0","0","0"]
        self.serialTimeOut=serialTimeOut
        self.prepareSerialListener()
        
    def prepareSerialListener (self):
        self.nfcInterfaces=[]
        for i in range(0,4):
            self.prepareSingleNfcListener(i)    

        
    def prepareSingleNfcListener (self, num):
        
        try:
            ser =serial.Serial(
                port=self.usbList[num],
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=self.serialTimeOut
            )
            print num
            print(" ACM  loaded")
            self.nfcInterfaces.append(ser)
        except:
            print num
            print(" ACM  not loaded")    

    def readSerialInput(self):
        io=["","","",""]
        for num, nfcInterface in enumerate (self.nfcInterfaces, 0):
            try:
                io[num]=nfcInterface.readline().decode('utf-8')[:-2]
               
            except:
                io[num]=""

        for num,msg in  enumerate(io, start=0):
            if msg not in self.lastMessageList[num]:
                print msg
                self.decodeMessage(msg)
                self.lastMessageList[num]=msg

    def decodeMessage(self,msg):
        if msg != "":
            msg.rstrip('\n')
            self.onIdDetected(msg)

    def startReadingLoop(self):
        self.isRunning=True
        while self.isRunning:
            self.readSerialInput()
            time.sleep(self.timeOut)
        
    def onIdDetected(self,msg):
        for l in self.listener:
            l.recievedMessage(msg)

    def addIdDetectedListener(self, listener):
        self.listener.append(listener)
    
    def Clean(self):
        self.isRunning=False
        