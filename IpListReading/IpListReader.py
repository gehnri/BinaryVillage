import json

class IpListReader:
    
    def __init__(self,filePath="Assets/ipListe.json"):
        self.filePath=filePath
    
    def getListOfChannelListener(self):
        channelListenerIps=[]
        with open(self.filePath) as json_file:
            data = json.load(json_file)
            for ip in data["channelListenerIp"]:
                channelListenerIps.append(ip)
        return channelListenerIps
    
    def getAdressOfFileDispatcher(self):
        dispatcherIp=""
        with open(self.filePath) as json_file:
            data = json.load(json_file)
            dispatcherIp=data["audioDispatcherIp"]
        return dispatcherIp

