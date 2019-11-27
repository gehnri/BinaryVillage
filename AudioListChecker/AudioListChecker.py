import os
import json
class AudioListChecker:


    def __init__(self, jsonAudioDictImporter,filePrefix="Assets/Sounds/",jsonFilePath="Assets/spellCheckErrorList.json"):
        self.jsonAudioDictImporter=jsonAudioDictImporter
        self.prefix=filePrefix
        self.listOfNotInFolder=[]
        self.jsonFilePath=jsonFilePath
        self.fileCountChecked=0

    def CheckListOfAudioFiles(self):
        audioList=self.jsonAudioDictImporter.prepareDictOfSounds().values()
    	for fileName in audioList:
            self.fileCountChecked+=1
            if not os.path.exists(self.prefix+fileName):
                self.SaveNameIfNotExists(fileName)
        self.SaveToErrorFile(self.listOfNotInFolder)

    def SaveNameIfNotExists(self,fileName):
        self.listOfNotInFolder.append(fileName)

    def SaveToErrorFile(self,listToWrite):
        print "Checked Filenamount:"
        print self.fileCountChecked

        if len(listToWrite)>0:
            print "Found error please check list in Assets"
        with open(self.jsonFilePath, 'w') as f:
            json.dump(listToWrite, f)
    
    #def CheckIfSoundIsPlayable():
