import pygame
from AudioPositionHolder import AudioPositionHolder
from  AngleToVolumeConverter import AngleToVolumeConverter

class AudioChannel:

    def __init__(self, initAudioFile, audioPositionHolder, filePrefix="Assets/Sounds/"):
        self.number=audioPositionHolder.id
        self.audioPosHolder=audioPositionHolder
        self.currentAudioFile=initAudioFile
        self.channel=pygame.mixer.Channel(audioPositionHolder.id)
        self.angleConverterLeft=AngleToVolumeConverter(self.audioPosHolder.maxVolAngle,self.audioPosHolder.minLeftVolAngle)
        self.angleConverterRight=AngleToVolumeConverter(self.audioPosHolder.minRightVolAngle,self.audioPosHolder.maxVolAngle)
        self.playAudioFile(filePrefix+self.currentAudioFile)
        self.oldAngle=-1
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

    def setVolumeBasedOnAngle(self, angle):
        if self.oldAngle!=angle:
            vol=0
            if angle < self.audioPosHolder.maxVolAngle and angle > self.audioPosHolder.minLeftVolAngle: 
                vol=self.angleConverterLeft.convertAngleIntoVolume(angle)
            elif angle >  self.audioPosHolder.maxVolAngle and angle < self.audioPosHolder.minRightVolAngle:
                volTemp=self.angleConverterRight.convertAngleIntoVolume(angle)
                vol=1.0-volTemp
            #print "Channel: " + str(self.number) +"  VOL:"+ str(vol)
            self.oldAngle=angle
            self.channel.set_volume(vol)
        
    
    def getId(self):
        return str(self.number)