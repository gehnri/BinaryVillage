from AudioHandler import AudioHandler 
from AngleConverter import AngleConverter
class OnObserveRotation:

    def __init__(self, audioHandler,angleConverter):
     
        self.audioHandler =audioHandler
        self.converter=angleConverter
        
    def onRotate(self,val):
        #change the volume of the channels
        angle=self.converter.convertStepInAngle(val)
        #pass degrees to all channels
        self.audioHandler.changeVolume(angle)

    
    