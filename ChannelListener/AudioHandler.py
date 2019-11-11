import pygame
from AudioChannel import AudioChannel
from AudioPositionHolder import AudioPositionHolder
class AudioHandler :
    
    def __init__(self,firstSoundFileName,consolInputManager,prefReader):
        pygame.init()
        pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2**12)
        self.prefReader=prefReader
        self.channelDict={}   
        self.firstSoundFileName=firstSoundFileName
        consolInputManager.getIntVal(self,"Who am I? - \n 0 = Main \n 1 = Rechts von Anfang \n 2= Gegenueber von Anfang \n 3= Links von Main ")
        

    def createChannel(self,file,positionHolder):
        return AudioChannel(file,positionHolder)

    
        
    def changeVolume(self, angle):
         for channeID in self.channelDict:
            self.channelDict[channeID].setVolumeBasedOnAngle(angle)

    

    def changeAudioFileOnChannel(self, channeIDNum, fileName):
        channeID=int(channeIDNum)
        print channeID
        print self.channelDict
        if channeID in self.channelDict:
            print "Playing  "+ fileName + " at CH "+channeIDNum
            self.channelDict[channeID].setSong(fileName)
        elif channeID is self.ownId:
            #set ownChannelSound
            print "Playing  "+ fileName + "on own"

            pass
        else:
            print "Cant find channel: "
            print (channeID)

    def  initChannel (self, val, prefReader):
            rechtsVonUrsprung=prefReader.getAngleOf("rechtsVonUrsprung")#(110,155,210)
            linksVonUrsprung=prefReader.getAngleOf("linksVonUrsprung")#(0,65,110)
            gegenUeber=prefReader.getAngleOf("gegenUeber")#(65,110,155)
            own=prefReader.getAngleOf("own")#(45,0,45)

            if val is 0:#Main
                self.ownId=0
                self.channelDict[1]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(1,rechtsVonUrsprung))
                self.channelDict[2]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(2,gegenUeber))
                self.channelDict[3]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(3,linksVonUrsprung))
                
                
            elif val is 1:#
                self.ownId=1
                self.channelDict[0]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(0,linksVonUrsprung))
                self.channelDict[2]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(2,gegenUeber))
                self.channelDict[3]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(3,rechtsVonUrsprung))
                
            elif val is 2:
                self.ownId=2
                self.channelDict[0] =self.createChannel(self.firstSoundFileName,AudioPositionHolder(0,gegenUeber))
                self.channelDict[1]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(1,linksVonUrsprung))
                self.channelDict[3]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(3,rechtsVonUrsprung))
                
            elif val is 3:
                self.ownId=3
                self.channelDict[0]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(0,rechtsVonUrsprung))
                self.channelDict[2]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(1,linksVonUrsprung))
                self.channelDict[1]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(3,gegenUeber))
                
            self.channelDict[self.ownId]=self.createChannel(self.firstSoundFileName,AudioPositionHolder(self.ownId,own))
    def callback(self,val):
            print "You chosse Channel: " + str(val)
            self.initChannel(val,self.prefReader)
