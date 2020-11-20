# https://popcorn16.tistory.com/122
from pymongo import MongoClient
from pymongo.cursor import CursorType 
from ..logging.logging import log_time
from ..config.config import JsonConfig 

host='192.168.40.65'
port=27017
username='root'
password='root12345!'
column_dict  = ['Player_name','Player_level','Player_icon','Player_tier','Player_win','Player_lose','Player_recent_time'] #Player_info Column

class MongoDBHandler:
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
    def insert_item(self, db_name, collection_name, column_dict, data):
        collection  = self.client[db_name][collection_name]
        results = list()

        for line in data:
            dict = {name: value for name, value in zip(column_dict, line)} # make new element
            res = collection.insert_one(dict) # insert element
            results.append(res)

        return results 
    
    def find_item(self, column_name, column_value, db_name, collection_name):
        collection  = self.client[db_name][collection_name]
        condition = self.create_condition(column_name, column_value)

        res = collection.find_one_item(condition)
        return res, condition 

    def delete_item(self, column_name, column_value, db_name, collection_name):
        result, condition = self.find_item(column_name, column_value, db_name, collection_name)
        if result is None:
            print(f"{condition} - 존재하지 않는 값입니다.")
        else:
            collection  = self.client[db_name][collection_name]
            result = collection.delete_one(condition)
        return result 

    def update_item(self, column_name, column_value, update_column, update_value, db_name, collection_name):
        result, condition = self.find_item(column_name, column_value, db_name, collection_name)

        if result is None:
            print(f"{condition} - 존재하지 않는 플레이어 값입니다.")
        else:
            collection = self.client[db_name][collection_name]
            new_value = {"$set": {update_column: update_value}} 
            result = collection.update_one(condition, new_value)
        
        return result

    def create_condition(self, column_name, column_value):
        return {str(column_name) : str(column_value)}
