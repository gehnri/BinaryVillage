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
        try:
            self.ser0 = serial.Serial(
                port=self.usbList[0], #'/dev/ttyACM0',
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=self.serialTimeOut
            )
            self.nfcInterfaces.append(self.ser0)
            print(" ACM 0  loaded")
        except:
            print(" ACM 0 not loaded")

        try:
            self.ser1 = serial.Serial(
                port=self.usbList[1],#'/dev/ttyACM1',
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=self.serialTimeOut
            )
            print(" ACM 1  loaded")
            self.nfcInterfaces.append(self.ser1)
        except:
            print(" ACM 1 not loaded")
        try:
            self.ser2 = serial.Serial(
                port=self.usbList[2],#'/dev/ttyACM2',
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=self.serialTimeOut
            )
            print(" ACM 2  loaded")

            self.nfcInterfaces.append(self.ser2)
        except:
            print(" ACM 2 not loaded")
        try:
            self.ser3 = serial.Serial(
                port=self.usbList[3],#'/dev/ttyACM3',
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=self.serialTimeOut
            )
            print(" ACM 3  loaded")
            self.nfcInterfaces.append(self.ser3)
        except:
            print(" ACM 3 not loaded")    
        
    def readSerialInput(self):
        io=["","","",""]
        for num, nfcInterface in enumerate (self.nfcInterfaces, 0):
            try:
                io[num]=nfcInterface.readline().decode('utf-8')[:-2]
               
            except:
                io[num]=""

        #io[0] = self.ser0.readline().decode('utf-8')[:-2]
        #io[1] = self.ser1.readline().decode('utf-8')[:-2]
        #io[2] = self.ser2.readline().decode('utf-8')[:-2]
        #io[3]=  self.ser3.readline().decode('utf-8')[:-2]

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
        while 1:
            self.readSerialInput()
            time.sleep(self.timeOut)
        
    def onIdDetected(self,msg):
        for l in self.listener:
            l.recievedMessage(msg)

    def addIdDetectedListener(self, listener):
        self.listener.append(listener)
        