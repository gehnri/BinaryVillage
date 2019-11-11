from ChannelListener.AudioHandler import AudioHandler
from time import sleep
from ChannelListener.inputHandler import ArduinoInputHandler
from ChannelListener.OnObserveRotation import OnObserveRotationm
from ChannelListener.RotaryConverter import RotaryConverter
from OSCHandler.OSCInputHandler import OSCInputHandler
from OSCHandler.OnOSCMessage import OnOSCMessage  
from ChannelListener.OSCMessageHandling.SoundMessageHandler import SoundMessageHandler
from ConsolInput.ConsolInputManager import ConsolInputManager
from IpListReading.IpChooser import IpChosser
from IpListReading.IpListReader import IpListReader
from ChannelListener.channelPrefReader import ChannelPrefReader

def start():
        prefReader=ChannelPrefReader()
        running=True
        sleeT=prefReader.getSleepTimeOut()

        cInputManager=ConsolInputManager()
        potiTr=prefReader.getPotiTreshold()
        converter=RotaryConverter(potiTr[0],potiTr[1])

        firstAudioFile=prefReader.getFirstAudioFile()
        audioHandler=AudioHandler(firstAudioFile,cInputManager,prefReader)

        observeRotation= OnObserveRotationm(audioHandler,converter)
        inputHandler= ArduinoInputHandler()
        inputHandler.addListener(observeRotation)

        soundMSGHandler=SoundMessageHandler(audioHandler)
        onOSCMessage =OnOSCMessage()
        onOSCMessage.addMessageHandler(soundMSGHandler)
        
        ipListReader=IpListReader()
        ipChooser=IpChosser(cInputManager,ipListReader)
        
        oscInputHandler= OSCInputHandler()
        oscInputHandler.registerCallBackListener(onOSCMessage)

        oscInputHandler.initServer(ipChooser)

        while running:
        
                inputHandler.checkRotation()
                sleep(sleeT)
        

if __name__ == '__main__':
    start()