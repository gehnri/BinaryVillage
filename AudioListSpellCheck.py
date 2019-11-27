from AudioListChecker.AudioListChecker import AudioListChecker
from SoundMessageDispatcher.JSONListImporter import JSONListImporter


def start():
    jsonListImporter=JSONListImporter()
    audioListCheker=AudioListChecker(jsonListImporter)
    audioListCheker.CheckListOfAudioFiles()
        

if __name__ == '__main__':
    start()
