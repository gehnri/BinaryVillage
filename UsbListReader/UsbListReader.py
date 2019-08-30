import json

class UsbListReader:
    
    def __init__(self,filePath="Assets/UsbList.json"):
        self.filePath=filePath
    
    def getUsbList(self):
        portList=[]
        with open(self.filePath) as json_file:
            data = json.load(json_file)
            for port  in data:
                portList.append(port)
        return portList

