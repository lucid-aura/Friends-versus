import sys
import os
from config import MongoDBConfig
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/loggings")
from loggings import log_time
from pymongo import MongoClient
from pymongo.cursor import CursorType


class DataDAO:
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

    @log_time
    def create_condition(self, column_name, column_value):
        return {str(column_name): str(column_value)}

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
        print("update")
        print(result)
        if result is None:
            print(f"{condition} - 존재하지 않는 이름입니다.")
        else:
            collection = self.client[db_name][collection_name]
            row_list = list(update_values.keys())
            for update_column in row_list:
                new_value = {"$set": {update_column: update_values[update_column]}}
                result = collection.update_one(condition, new_value)
        return result

    def update_friendslist(self, id, friendInfo):
        collection = self.client["USER"]["INFO"]
        condition = self.create_condition('userid', id)
        new_value = {"$set": friendInfo}
        result = collection.update_one(condition, new_value)
        return result

    def count_document(self, db_name, collection_name):
        collection = self.client[db_name][collection_name]
        cnt = collection.find().count()
        return cnt

    def update_player(self, name, update_values):
        self.update_row("name", name, update_values, "DATA", "PLAYER")