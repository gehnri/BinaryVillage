class ConsolInputManager:

    def __init__(self):
        self.extMsfg="/n Type 'exit_now' if you want to stop input."

    
    def getIntVal(self,callBackObject,msg):
         finMSg=msg+self.extMsfg
         val = int(input(finMSg))
         callBackObject.callback(val)

    def getStringVal(self,callBackObj,msg):
        finMsg=msg+self.extMsfg
        try: 
            val=str(input(finMsg))
            print "Input = "+ val
            if "exit_now" in val:
                print ("Take another nfc card or leave by ctrl+c")

            else:
                callBackObj.callback(val)
        except:
             print "Couldnt read the string dont forget the quotation marks"
             self.getStringVal(callBackObj,msg)