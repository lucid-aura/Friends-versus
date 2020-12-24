import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/model")
from data_dao import DataDAO
import json
from bson import json_util

class DataService:

    def __init__(self):
        self.data_dao = DataDAO()
        
    def insert_playerInfo(self, playerInfo):
        result = self.data_dao.insert_item("DATA", "PLAYER", playerInfo)
        #print(result)
        return result

    def insert_champions_summary(self, champion_summary):
        return self.data_dao.insert_item("DATA", "CHAMPIONS_SUMMARY", champion_summary)

    def get_champions_summary(self):
        collection = self.data_dao.client["DATA"]["CHAMPIONS_SUMMARY"]
        #print(list(collection.find()))
        summary_list = list(collection.find())
        summary_json = json.dumps(summary_list, default=json_util.default, ensure_ascii = False)
        return summary_json

    def get_champion_ids(self):
        result = self.data_dao.find_items("DATA", "CHAMPIONS_SUMMARY", "id")
        return result

    def insert_champion_data(self, champion_data):
        result = self.data_dao.find_item("DATA", "CHAMPION", "id", champion_data['id'])
        if result is None:
            return self.data_dao.insert_item("DATA", "CHAMPION", champion_data)

    def get_champion_data(self, champion_id):
        result = self.data_dao.find_item("DATA", "CHAMPION", "id", champion_id)
        return result

    def find_playerInfo_by_name(self, name):
        result = self.data_dao.find_item("DATA", "PLAYER", "name", name)
        #print(result)
        return result
 