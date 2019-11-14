
from ChannelListener.AudioHandler import AudioHandler
from time import sleep
from SysClean.SysCleaner import SysCleaner
from ChannelListener.PotiInputReciever import PotiInputReciever
from ChannelListener.OnObserveRotation import OnObserveRotation
from OSCHandler.OSCInputHandler import OSCInputHandler
from OSCHandler.OnOSCMessage import OnOSCMessage  
from ChannelListener.OSCMessageHandling.SoundMessageHandler import SoundMessageHandler
from ConsolInput.ConsolInputManager import ConsolInputManager
from IpListReading.IpChooser import IpChosser
from IpListReading.IpListReader import IpListReader
from ChannelListener.channelPrefReader import ChannelPrefReader
from  ChannelListener.AngleConverter import AngleConverter
def start():

        sysCleaner =SysCleaner()
        prefReader=ChannelPrefReader()
        running=True
        sleeT=prefReader.getSleepTimeOut()

        cInputManager=ConsolInputManager()
        potiTr=prefReader.getPotiTreshold()
        converter=AngleConverter(potiTr[0],potiTr[1])

        firstAudioFile=prefReader.getFirstAudioFile()
        audioHandler=AudioHandler(firstAudioFile,cInputManager,prefReader)

        observeRotation= OnObserveRotation(audioHandler,converter)
        potiInputReciever= PotiInputReciever()
        potiInputReciever.addListener(observeRotation)

        soundMSGHandler=SoundMessageHandler(audioHandler)
        onOSCMessage =OnOSCMessage()
        onOSCMessage.addMessageHandler(soundMSGHandler)
        
        ipListReader=IpListReader()
        ipChooser=IpChosser(cInputManager,ipListReader)
        
        oscInputHandler= OSCInputHandler()
        oscInputHandler.registerCallBackListener(onOSCMessage)

        oscInputHandler.initServer(ipChooser)
        
        sysCleaner.addCleanListener(audioHandler)
        sysCleaner.addCleanListener(oscInputHandler)

        while running:
        
                potiInputReciever.checkRotation()
                sleep(sleeT)
        

if __name__ == '__main__':
    start()


