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
from NfcReader.SaveIdsToJson import SaveIdToJson
from ConsolInput.ConsolInputManager import ConsolInputManager
 
def start ():
    print "Start reading NFC... \n ACHTUNG: \n \t Vergiss nicht die Anfuehrungsstriche bei der Eingabe \n\t von Sounds \n !!!!"

    cInputManager=ConsolInputManager()
    prefReader=DispatcherPrefReader()
    usbListReader=UsbListReader()
    usbPortList=usbListReader.getUsbList()
    nfcSerialReader=NfcSerialReader(usbPortList,prefReader.getSleepTimeOut(),prefReader.getSerialTimeOut())
    idSaver=SaveIdToJson(cInputManager)
    nfcSerialReader.addIdDetectedListener(idSaver)
    nfcSerialReader.startReadingLoop()
    
if __name__ == '__main__':
    start()