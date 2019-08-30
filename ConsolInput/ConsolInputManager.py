class ConsolInputManager:

    def __init__(self):
        pass
    
    def getIntVal(self,callBackObject,msg):
         val = int(input(msg))
         callBackObject.callback(val)

    def getStringVal(self,callBackObj,msg):
        try: 
            val=str(input(msg))
            print "Input = "+ val
            callBackObj.callback(val)
        except:
            print "Couldnt read the string dont forget the quotation marks"
            self.getStringVal(callBackObj,msg)