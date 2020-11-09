import json 

class JsonConfig:
    def __init__(self, configFile="Develop.json"):
        assert configFile != ""
        self.configFile = configFile
        self.config = None 

        self.load() 
        

    def load(self):
        # 설정 파일을 로딩한다.
        with open(self.configFile, 'r') as jsonFile:
            self.config = json.load(jsonFile)
        
        





