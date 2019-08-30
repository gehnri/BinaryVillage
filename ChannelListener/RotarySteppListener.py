class RotarySteppListener:
    def __init__(self,maxSteps):
        self.steps=0
        self.maxSteps=maxSteps
        
    def onLeft(self):
        self.steps-=1
        if self.steps<0:
            self.steps=0
    
    def onRight(self):
        self.steps+=1
        if self.steps > self.maxSteps:
            self.steps=self.maxSteps
            
    def getCurrentStep(self):
        return self.steps