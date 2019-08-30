class IpChosser:

    def __init__(self, cInputManager, ipListReader):
        self.cInputManager=cInputManager
        self.ipListReader=ipListReader

    def chooseIpFromJsonList(self):
        self.adressList=self.ipListReader.getListOfChannelListener()
        inputMessaqge="Choose an ip according to channel \n"
        for num, ip in enumerate (self.adressList, start=0):
            inputMessaqge +="\t CH: "+ str(num) + " = "+ ip + "\n"
        
        self.cInputManager.getIntVal(self,inputMessaqge)
    
    def callback(self,numVal):
        self.currentIp=self.adressList[numVal]
    
    def getIpAdress(self):
        self.chooseIpFromJsonList()
        print "You chose :" + self.currentIp
        return self.currentIp