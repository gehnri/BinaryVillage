class IDChecker:#

    def __init__(self, idSondDict):
        self.idSondDict=idSondDict
    
    def checkForId(self, id):
        if id in self.idSondDict:
            return True
        else: 
            return False