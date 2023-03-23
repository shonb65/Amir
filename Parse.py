import json
import FileHandler


class Parse:
    def __init__(self, unParsedFile):
        self.parsedFile = json.loads(unParsedFile)
        return self.parsedFile
    

