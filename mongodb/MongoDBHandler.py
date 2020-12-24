import sys
import os
# import json
# from bson import json_util
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/loggings")
from loggings import log_time

from model.data_dao import DataDAO
from services.data_service import DataService
from services.image_service import ImageService

# #host='192.168.200.163'
# host='192.168.40.52' #PC 설정에 따라 다르다. window 일경우 C:\Windows\System32\drivers\etc\hosts 파일에 docker 주소 및 포트가 있음.
# host='http://host.docker.internal'
# port=27017
# username='root'
# password='root12345!'

class MongoDBHandler:
    def __init__(self):
        self.data_dao = DataDAO()
        self.data_service = DataService()
        self.image_service = ImageService()

    @log_time
    def insert_item(self, db_name, collection_name, input_data):
        return self.data_dao.insert_item(db_name, collection_name, input_data)


    def insert_items(self, db_name, collection_name, input_data):
        return self.data_dao.insert_items(db_name, collection_name, input_data)


    def find_item(self, db_name, collection_name, column_name, column_value):
        return self.data_dao.find_item(db_name, collection_name, column_name, column_value)

    def find_items(self, db_name, collection_name, name):
        return self.data_dao.find_itemsdb_name, collection_name, name()

    def delete_item(self, column_name, column_value, db_name, collection_name):
        return self.data_dao.delete_item(column_name, column_value, db_name, collection_name)

    def update_item(self, column_name, column_value, update_column, update_value, db_name, collection_name):
        return self.data_dao.update_item(column_name, column_value, update_column, update_value, db_name, collection_name)

    def update_row(self, column_name, column_value, update_values , db_name, collection_name):
        return self.data_dao.update_row(column_name, column_value, update_values , db_name, collection_name)

    def count_document(self, db_name, collection_name):
        return self.data_dao.count_document(db_name, collection_name)

    def update_player(self, name, update_values):
        self.data_dao.update_row("name", name, update_values, "DATA", "PLAYER")

    def check_duplicate(self, db_name, collection_name, key):
        collection = self.client[db_name][collection_name]
        collection.create_index([(key, pymongo.ASCENDING)], unique=True)

    def insert_playerInfo(self, playerInfo):
        return self.data_service.insert_playerInfo("DATA", "PLAYER", playerInfo)

    def insert_champions_summary(self, champion_summary):
        return self.data_service.insert_champions_summary("DATA", "CHAMPIONS_SUMMARY", champion_summary)

    def get_champions_summary(self):
        return self.data_service.get_champions_summary()

    def get_champion_ids(self):
        return self.data_service.get_champion_ids()

    def insert_champion_data(self, champion_data):
        return self.data_service.insert_champion_data(champion_data)

    def get_champion_data(self, champion_id):
        return self.data_service.get_champion_data(champion_id)

    def find_playerInfo_by_name(self, name):
        return self.data_service.find_playerInfo_by_name(name)
 
    def get_champion_skin_ids(self, champion_id):
        return self.image_service.get_champion_skin_ids(champion_id)

    def get_champion_skin_number(self, champion_id):
         return self.image_service.get_champion_skin_number(champion_id)
        
    def find_champion_loading_images_by_skin_number(self, skin_number):
        return self.image_service.find_champion_loading_images_by_skin_number(skin_number)

    def insert_champion_loading_skin(self, input_data):
        return self.image_service.insert_champion_loading_skin(input_data)

    def get_champion_loading_skin(self, champion_skin_number):
        return self.image_service.get_champion_loading_skin(champion_skin_number)
           
           
    def find_champion_splash_images_by_skin_number(self, skin_number):
        return self.image_service.find_champion_splash_images_by_skin_number(skin_number)

    def insert_champion_splash_skin(self, input_data):
        return self.image_service.insert_champion_splash_skin(input_data)

    def get_champion_splash_skin(self, champion_skin_number):
        return self.image_service.get_champion_splash_skin(champion_skin_number)

    def insert_champion_square_image(self, input_data):
        return self.image_service.insert_champion_square_image(input_data)

    def get_champion_square_image(self, champion_id):
        return self.image_service.get_champion_square_image(champion_id)

    def find_champion_square_image_by_champion_id(self, champion_id):
        return self.image_service.find_champion_square_image_by_champion_id(champion_id)

    def insert_champion_spell_images(self, input_data):
        return self.image_service.insert_champion_spell_images(input_data)

    def get_champion_spell_images_by_champion_id(self, champion_id):
        return self.image_service.get_champion_spell_images_by_champion_id(champion_id)

    def find_champion_spell_images_by_champion_id(self, champion_id):
        return self.image_service.find_champion_spell_images_by_champion_id(champion_id) 
