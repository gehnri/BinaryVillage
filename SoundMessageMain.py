from SoundMessageDispatcher.JSONListImporter import JSONListImporter
from OSCHandler.OSCInputHandler import OSCInputHandler
from OSCHandler.OnOSCMessage import OnOSCMessage
from SoundMessageDispatcher.GetIDViaOsc import GetIDViaOsc
from SoundMessageDispatcher.CheckForIdInDict import IDChecker
from SoundMessageDispatcher.SendOSCMessageToAllListener import OSCSoundSender
from IpListReading.IpListReader import IpListReader
from SoundMessageDispatcher.GetIDViaSerial import GetIdViaSerial
from NfcReader.NfcSerialReader import NfcSerialReader
from UsbListReader.UsbListReader import UsbListReader
from SoundMessageDispatcher.DispatcherPrefReader import DispatcherPrefReader

def start ():
    prefReader=DispatcherPrefReader()
    jsonRead=JSONListImporter()
    soundDict=jsonRead.prepareDictOfSounds()
    
    ipListReader=IpListReader()
    
    listOfAllChannelListener=ipListReader.getListOfChannelListener()
    sender=OSCSoundSender(listOfAllChannelListener)
    idChecker=IDChecker(soundDict)

    getIDViaSerial=GetIdViaSerial(idChecker,sender,soundDict)
   
    usbListReader=UsbListReader()
    usbPortList=usbListReader.getUsbList()
    nfcSerialReader=NfcSerialReader(usbPortList,prefReader.getSleepTimeOut(),prefReader.getSerialTimeOut())
    nfcSerialReader.addIdDetectedListener(getIDViaSerial)
    nfcSerialReader.startReadingLoop()
    
if __name__ == '__main__':
    start()