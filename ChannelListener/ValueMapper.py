
class ValueMapper(object):
    def __init__(self):
        pass
    

    def mapValues(self,OldValue,OldMax,OldMin,NewMax, NewMin):
        OldRange = (OldMax - OldMin)
        if OldRange == 0:
            NewValue = NewMin
        else :
            NewRange = (NewMax - NewMin)  
            NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
        
        if NewValue<NewMin:
            NewValue=NewMin
        
        if NewValue>NewMax:
            NewValue=NewMax
            
        return NewValue