class AudioPositionHolder:
    
    def __init__(self,id,volAngle):
        self.id =id
        self.minLeftVolAngle=volAngle[0]
        self.maxVolAngle=volAngle[1]
        self.minRightVolAngle=volAngle[2]
        