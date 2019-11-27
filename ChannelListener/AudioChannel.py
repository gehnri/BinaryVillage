import pygame
from AudioPositionHolder import AudioPositionHolder
from  AngleToVolumeConverter import AngleToVolumeConverter
import os

class AudioChannel:

    def __init__(self, initAudioFile, audioPositionHolder, filePrefix="Assets/Sounds/"):
        self.number=audioPositionHolder.id
        self.audioPosHolder=audioPositionHolder
        self.currentAudioFile=initAudioFile
        self.currentAudio="file"
        self.filePrefix=filePrefix

        self.channel=pygame.mixer.Channel(audioPositionHolder.id)
        self.endEvent=pygame.USEREVENT + self.number
        self.channel.set_endevent(self.endEvent)

        self.angleConverterLeft=AngleToVolumeConverter(self.audioPosHolder.maxVolAngle,self.audioPosHolder.minLeftVolAngle)
        self.angleConverterRight=AngleToVolumeConverter(self.audioPosHolder.minRightVolAngle,self.audioPosHolder.maxVolAngle)
        self.playAudioFile(filePrefix+self.currentAudioFile)
        self.oldAngle=-1
        self.noiseFile="noise.wav"
        self.noiseFile = pygame.mixer.Sound(self.filePrefix+self.noiseFile)


    def setSong(self,fileName):
        if os.path.exists(self.filePrefix+fileName):
            if fileName!=self.currentAudioFile:
                self.channel.set_endevent(0)
                self.currentAudioFile=self.filePrefix+fileName
                self.playAudioFile(self.currentAudioFile)
                print "Playing"
                print self.filePrefix+fileName
                self.channel.set_endevent(self.endEvent)
        else:
            print "Cant play:"
            print self.filePrefix+fileName 

        
    def playAudioFile(self,fileName):
        self.currentSound = pygame.mixer.Sound(fileName)
        self.channel.play(self.currentSound)
        self.currentAudio="file"
    
    def playNoise(self):
        if self.currentAudio in "file":
            print self.noiseFile
            self.currentAudio="noise"
            self.channel.play(self.noiseFile)
        else:
            print self.currentAudioFile
            self.channel.play(self.currentSound)
            self.currentAudio="file"
            

    def stopAll(self):
        self.channel.set_endevent(0)
        self.channel.stop()
        
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