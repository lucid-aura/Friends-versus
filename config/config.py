import json
import os
import socket

class JsonConfig:
    #def __init__(self, configFile="../data/Champion_one.json"):
        # 다른 json 파일도 선택적으로 읽을 수 있게 수정해야한다.
    def __init__(self, configFile):
        assert configFile != ""
        self.configFile = configFile
        self.load()
        
    def load(self):
        # 설정 파일을 로딩한다.
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, self.configFile)
        with open(abs_file_path, 'r') as jsonFile:
            self.config = json.load(jsonFile)
        print("Load File ", self.config)   
        self.__dict__ = self.config

class FlaskConfig(JsonConfig):
    SECRET_KEY = os.environ.get('SECRET>_KEY', "my_secret_key")
    MAINTAINER = "HSH"

    def __init__(self, configFile):
        super(FlaskConfig, self).__init__(configFile)


class MongoDBConfig(object):
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        self.host=IP
        self.port=27017
        self.username='root'
        self.password='root12345!'