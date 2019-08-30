from AudioHandler import AudioHandler 
from RotarySteppListener import RotarySteppListener
from RotaryConverter import RotaryConverter
class OnObserveRotationm:

    def __init__(self, audioHandler,rotaryConverter):
        #nothing yet
        self.audioHandler =audioHandler
        self.converter=rotaryConverter
    def onRotate(self,val):
        #change the volume of the channels
        deg=self.converter.convertStepInDegrees(val)
        #pass degrees to all channels
        self.audioHandler.changeVolume(deg)

    
    