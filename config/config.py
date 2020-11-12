import json
import os

class JsonConfig:
    #def __init__(self, configFile="../data/Champion_one.json"):
        # 다른 json 파일도 선택적으로 읽을 수 있게 수정해야한다.
    def __init__(self, configFile="../data/Champion.json"):
        assert configFile != ""
        self.configFile = configFile
        self.config = None 
        self.load()
        

    def load(self):
        # 설정 파일을 로딩한다.
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, self.configFile)
        with open(abs_file_path, 'r') as jsonFile:
            self.config = json.load(jsonFile)
        




