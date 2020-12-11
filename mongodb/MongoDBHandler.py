# https://popcorn16.tistory.com/122
from pymongo import MongoClient
from pymongo.cursor import CursorType
import pymongo
import sys
import os
import json
from bson import json_util
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/loggings")
from loggings import log_time
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/config")
from config import JsonConfig
from config import MongoDBConfig
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/data")
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/hyh_json_handler")
from JsonParser import JsonParser

print(os.path.dirname(__file__))
# #host='192.168.200.163'
# host='192.168.40.52' #PC 설정에 따라 다르다. window 일경우 C:\Windows\System32\drivers\etc\hosts 파일에 docker 주소 및 포트가 있음.
# host='http://host.docker.internal'
# port=27017
# username='root'
# password='root12345!'

class MongoDBHandler:
    def __init__(self):
        self.mongodbconfig = MongoDBConfig()
        self.host = self.mongodbconfig.host
        self.port = self.mongodbconfig.port
        self.username = self.mongodbconfig.username
        self.password = self.mongodbconfig.password

        self.client = MongoClient(host=self.host,
                                  port=self.port,
                                  username=self.username,
                                  password=self.password)
        
        self.develop_json = JsonConfig("Develop.json") # Develope Json 파일 열고 로드

    @log_time
    def insert_item(self, db_name, collection_name, input_data):
        collection = self.client[db_name][collection_name]
        res = collection.insert_one(input_data)  # insert element
        results = list()
        results.append(res)
        return results


    def insert_items(self, db_name, collection_name, input_data):
        collection = self.client[db_name][collection_name]
        res = collection.insert_many(input_data)
        results = list()
        results.append(res)
        return results


    def find_item(self, db_name, collection_name, column_name, column_value):
        collection = self.client[db_name][collection_name]
        condition = self.create_condition(column_name, column_value)
        res = collection.find_one(condition)
        #result = json.dumps(res, default=)
        #print("타입은 ", type(result))
        #return json.dumps(res, ensure_ascii=False)
        return res

    def find_items(self, db_name, collection_name, name):
        collection = self.client[db_name][collection_name]
        values = list()
        for doc in collection.find():
            value = str(doc[name])
            values.append(value)
        return values

    def delete_item(self, column_name, column_value, db_name, collection_name):
        result, condition = self.find_item(db_name, collection_name, column_name, column_value)
        if result is None:
            print(f"{condition} - 존재하지 않는 이름입니다.")
        else:
            collection = self.client[db_name][collection_name]
            result = collection.delete_one(condition)
        return result

    def update_item(self, column_name, column_value, update_column, update_value, db_name, collection_name):
        result, condition = self.find_item(db_name, collection_name, column_name, column_value)

        if result is None:
            print(f"{condition} - 존재하지 않는 이름입니다.")
        else:
            collection = self.client[db_name][collection_name]
            new_value = {"$set": {update_column: update_value}}
            result = collection.update_one(condition, new_value)
        return result

    def update_row(self, column_name, column_value, update_values , db_name, collection_name):
        result, condition = self.find_item(db_name, collection_name, column_name, column_value)
        if result is None:
            print(f"{condition} - 존재하지 않는 이름입니다.")
        else:
            collection = self.client[db_name][collection_name]
            row_list = list(update_values.keys())
            for update_column in row_list:
                new_value = {"$set": {update_column: update_values[update_column]}}
                result = collection.update_one(condition, new_value)
        return result

    def count_document(self, db_name, collection_name):
        collection = self.client[db_name][collection_name]
        cnt = collection.find().count()
        return cnt

    def update_player(self, name, update_values):
        self.update_row("name", name, update_values, "DATA", "PLAYER")

    def create_condition(self, column_name, column_value):
        return {str(column_name): str(column_value)}

    def check_duplicate(self, db_name, collection_name, key):
        collection = self.client[db_name][collection_name]
        collection.create_index([(key, pymongo.ASCENDING)], unique=True)

    def insert_playerInfo(self, playerInfo):
        result = self.insert_item("DATA", "PLAYER", playerInfo)
        #print(result)
        return result

    def insert_champions_summary(self, champion_summary):
        return self.insert_item("DATA", "CHAMPIONS_SUMMARY", champion_summary)

    def get_champions_summary(self):
        collection = self.client["DATA"]["CHAMPIONS_SUMMARY"]
        #print(list(collection.find()))
        summary_list = list(collection.find())
        summary_json = json.dumps(summary_list, default=json_util.default, ensure_ascii = False)
        return summary_json

    def insert_champion_data(self, champion_data):
        result = self.find_item("DATA", "CHAMPION", "id", champion_data['id'])
        if result is None:
            return self.insert_item("DATA", "CHAMPION", champion_data)

    def get_champion_data(self, champion_id):
        result = self.find_item("DATA", "CHAMPION", "id", champion_id)
        return result


    def find_playerInfo_by_name(self, name):
        result = self.find_item("DATA", "PLAYER", "name", name)
        #print(result)
        return result

    def insert_champion_loading_skin(self, input_data):
        result = self.find_item("IMG", "LOADING", "champion_skin_id", input_data['champion_skin_id'])
        if result is None:
            result = self.insert_item("IMG", "LOADING", input_data)
        return result

    def get_champion_loading_skin(self, champion_skin_id):
        result = self.find_item("IMG", "LOADING", 'champion_skin_id', champion_skin_id)
        return result
            