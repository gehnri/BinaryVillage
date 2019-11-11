from AudioHandler import AudioHandler 
from RotarySteppListener import RotarySteppListener
from AngleConverter import AngleConverter
class OnObserveRotationm:

    def __init__(self, audioHandler,angleConverter):
        #nothing yet
        self.audioHandler =audioHandler
        self.converter=angleConverter
    def onRotate(self,val):
        #change the volume of the channels
        angle=self.converter.convertStepInAngle(val)
        #pass degrees to all channels
        self.audioHandler.changeVolume(angle)

    
    