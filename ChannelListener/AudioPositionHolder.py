class AudioPositionHolder:
    
    def __init__(self,id,volDegrees):
        self.id =id
        self.minLeftVolDegree=volDegrees[0]
        self.maxVolDegree=volDegrees[1]
        self.minRightVolDegree=volDegrees[2]
        