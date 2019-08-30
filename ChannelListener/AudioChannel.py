import pygame
from AudioPositionHolder import AudioPositionHolder
from  DegreeToVolumeConverter import DegreeToVolumeConverter

class AudioChannel:

    def __init__(self, initAudioFile, audioPositionHolder, filePrefix="Assets/Sounds/"):
        self.number=audioPositionHolder.id
        self.audioPosHolder=audioPositionHolder
        self.currentAudioFile=initAudioFile
        self.channel=pygame.mixer.Channel(audioPositionHolder.id)
        self.degreeConverterLeft=DegreeToVolumeConverter(self.audioPosHolder.maxVolDegree,self.audioPosHolder.minLeftVolDegree)
        self.degreeConverterRight=DegreeToVolumeConverter(self.audioPosHolder.minRightVolDegree,self.audioPosHolder.maxVolDegree)
        self.playAudioFile(filePrefix+self.currentAudioFile)
        self.oldDegrees=-1
        self.filePrefix=filePrefix

    def setSong(self,fileName):
        if fileName!=self.currentAudioFile:
            self.currentAudioFile=self.filePrefix+fileName
            self.playAudioFile(self.currentAudioFile)
        print "Playing"
        print self.filePrefix+fileName
    
    def playAudioFile(self,fileName):
        audioFile = pygame.mixer.Sound(fileName)
        self.channel.play(audioFile,-1)

    def setVolumeBasedOnDegree(self, degrees):
        if self.oldDegrees!=degrees:
            vol=0
            if degrees < self.audioPosHolder.maxVolDegree and degrees > self.audioPosHolder.minLeftVolDegree: 
                vol=self.degreeConverterLeft.convertDegreesInVolume(degrees)
            elif degrees >  self.audioPosHolder.maxVolDegree and degrees < self.audioPosHolder.minRightVolDegree:
                volTemp=self.degreeConverterRight.convertDegreesInVolume(degrees)
                vol=1.0-volTemp
            #print "Channel: " + str(self.number) +"  VOL:"+ str(vol)
            self.oldDegrees=degrees
            self.channel.set_volume(vol)
        
    
    def getId(self):
        return str(self.number)