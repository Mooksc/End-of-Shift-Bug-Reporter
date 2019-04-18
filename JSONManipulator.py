import json

class JSONManipulator:

    def __init__(self, path, operation):
        try:
            loadedJSON = json.load(open(path, operation))
            self.path = path
            self.loadedJSON = loadedJSON
            print("loaded JSON as \'self.loadedJSON\'")
        except:
            try:
                loadedJSON = json.load(open(path, "x"))
                self.path = path
                self.loadedJSON = loadedJSON
                print("loaded JSON as \'self.loadedJSON\'")
            except:
                print("JSON Exists")
                try:
                    loadedJSON = json.load(open(path, "r"))
                    self.path = path
                    self.loadedJSON = loadedJSON
                    print("loaded JSON as \'self.loadedJSON\'")
                except:
                    print("JSON has no data. Creating sample data...")
                    loadedJSON = json.dump({"2": "b"}, open(path, "w"), indent=4)
                    self.path = path
                    self.loadedJSON = loadedJSON
                    print("loaded JSON as \'self.loadedJSON\'")

    def dumpJSON(self, output):
        json.dump(output, open(self.path, "w+"),indent=4)
        self.dumpedJSON = json.load(open(self.path, "r"))
        print("dumped JSON as \'self.dumpedJSON\'")

    def appendJSON(self, outputK, outputV):
        i = 0
        l = len(outputK)
        while i < l:
            self.loadedJSON[outputK[i]] = outputV[i]
            i +=1
        json.dump(self.loadedJSON, open(self.path, "w+"), indent=4)

    def removePair(self, keys):
        for i in keys:
            self.loadedJSON.pop(i)
            json.dump(self.loadedJSON, open(self.path, "w+"), indent=4)

    def addChildPair(self, parentKey, dictObject):

        snapshot = self.loadedJSON[parentKey]

        self.loadedJSON[parentKey] = snapshot[0], dictObject

        json.dump(self.loadedJSON, open(self.path, "r+"), indent=4)

    def appendChildList(self, parentKey, output):

        parentList = self.loadedJSON[parentKey]
        for i in output:

            if i not in parentList:

                parentList.append(i)

        json.dump(self.loadedJSON, open(self.path, "w+"), indent=4)
