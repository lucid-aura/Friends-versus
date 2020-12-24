import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/model")
from data_dao import DataDAO
import json
from bson import json_util

class UserService:
    def __init__(self):
        self.data_dao = DataDAO()
    
    def insert_userinfo(self, userInfo):
        result = self.data_dao.insert_item("USER", "INFO", userInfo)
        return result

    def get_userinfo(self):
        result = self.data_dao.find_item("USER", "INFO", "id", userInfo['id'])
        #print(list(collection.find()))
        return result
