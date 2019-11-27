from AudioListChecker.AudioListChecker import AudioListChecker
from SoundMessageDispatcher.JSONListImporter import JSONListImporter
from AudioListChecker.AudioPlayChecker import AudioPlayChecker
from ChannelListener.channelPrefReader import ChannelPrefReader
from ConsolInput.ConsolInputManager import ConsolInputManager
from ChannelListener.AudioHandler import AudioHandler

def start():
    jsonListImporter=JSONListImporter()
    
    prefReader=ChannelPrefReader()

    cInputManager=ConsolInputManager()
    potiTr=prefReader.getPotiTreshold()

    firstAudioFile=prefReader.getFirstAudioFile()
    audioHandler=AudioHandler(firstAudioFile,cInputManager,prefReader)

    audioCheck=AudioPlayChecker(audioHandler,jsonListImporter)
    audioCheck.CheckAudioFromList()

if __name__ == '__main__':
    start()
