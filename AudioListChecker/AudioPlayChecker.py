from time import sleep
import os
import json
class AudioPlayChecker:

    def __init__(self, audioHandler,jsonAudioDictImporter,filePrefix="Assets/Sounds/",jsonFilePath="Assets/audioErrorList.json"):
        self.audioHandler=audioHandler
        self.jsonAudioDictImporter=jsonAudioDictImporter
        self.prefix=filePrefix
        self.listOfNotInFolder=[]
        self.jsonFilePath=jsonFilePath
        self.fileCountChecked=0
        self.listOfNotPlayable=[]
    def CheckAudioFromList(self):
        audioList=self.jsonAudioDictImporter.prepareDictOfSounds().values()
        for i in range(1,4):
            self.audioHandler.StopChannel(i)

        for fileName in audioList:
            self.fileCountChecked+=1
            if os.path.exists(self.prefix+fileName):
                try:
                    self.audioHandler.changeAudioFileOnChannel( 0, fileName)
                    print "Play"+fileName
                except:
                    self.listOfNotPlayable.append(fileName)
                    print "Cant play"+fileName
                sleep(3)
        print(self.listOfNotPlayable)
        if len(self.listOfNotPlayable)>0:
            print "Found error please check list in Assets"
        with open(self.jsonFilePath, 'w') as f:
            json.dump(self.listOfNotPlayable, f)