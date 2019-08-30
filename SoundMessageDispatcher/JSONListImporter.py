import json

class JSONListImporter:

    def __init__(self):
        self.fileName="Assets/audioList.json"

    def prepareDictOfSounds(self):
        songDict={}
        with open(self.fileName) as json_file:
            data = json.load(json_file)
            for id  in data:
                songDict[id]=data[id]
                print "ID "+id + "Song: " + data [id]
        return songDict
                 