# https://popcorn16.tistory.com/122
from pymongo import MongoClient
from pymongo.cursor import CursorType
import pymongo
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/loggings")
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/config")
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/data")
from loggings import log_time
from config import JsonConfig
#from ..logging.logging import log_time
#from ..config.config import JsonConfig


host='192.168.40.52' #PC 설정에 따라 다르다. window 일경우 C:\Windows\System32\drivers\etc\hosts 파일에 docker 주소 및 포트가 있음.
port=27017
username='root'
password='root12345!'

class MongoDBHandler:
    def __init__(self):
        self.client = MongoClient(host=host,
                                  port=port,
                                  username=username,
                                  password=password)

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self.client = MongoClient(host=self.host,
                                  port=self.port,
                                  username=self.username,
                                  password=self.password)

    @log_time
    def insert_item(self, db_name, collection_name, input_data):
        collection = self.client[db_name][collection_name]
        results = list()
        res = collection.insert_one(input_data)  # insert element
        results.append(res)
        return results


    def insert_items(self, db_name, collection_name, input_data):
        collection = self.client[db_name][collection_name]
        res = collection.insert_many(input_data)
        results = list()
        results.append(res)
        return results


    def find_item(self, column_name, column_value, db_name, collection_name):
        collection = self.client[db_name][collection_name]
        condition = self.create_condition(column_name, column_value)
        res = collection.find_one(condition)
        print(res)
        return res, condition

    def delete_item(self, column_name, column_value, db_name, collection_name):
        result, condition = self.find_item(column_name, column_value, db_name, collection_name)
        if result is None:
            print(f"{condition} - 존재하지 않는 이름입니다.")
        else:
            collection = self.client[db_name][collection_name]
            result = collection.delete_one(condition)
        return result


    def update_item(self, column_name, column_value, update_column, update_value, db_name, collection_name):
        result, condition = self.find_item(column_name, column_value, db_name, collection_name)

        if result is None:
            print(f"{condition} - 존재하지 않는 이름입니다.")
        else:
            collection = self.client[db_name][collection_name]
            new_value = {"$set": {update_column: update_value}}
            result = collection.update_one(condition, new_value)
        return result

    def create_condition(self, column_name, column_value):
        return {str(column_name): str(column_value)}


    def check_version(self):
        json = JsonConfig()
        version = json.client_version()
        #version = [version]
        print(version)
        self.insert_item("Integrity", "Client_version", [version])
        # if collection != version:
        #     # 버전을 비교하고 업데이트 하는 기능 필요
        #     new_value = {"$set": {"version": version}}
        #     result = collection.update_one(new_value)
        return version

    def check_duplicate(self, db_name, collection_name, key):
        collection = self.client[db_name][collection_name]
        collection.create_index([(key, pymongo.ASCENDING)], unique=True)
