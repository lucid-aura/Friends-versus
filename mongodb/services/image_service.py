import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/model")
from data_dao import DataDAO

class ImageService:
    def __init__(self):
        self.data_dao = DataDAO()

    def get_champion_skin_ids(self, champion_id):
        result = self.data_dao.find_item("DATA", "CHAMPION", "id", champion_id)
        if result == None:
            return None
        res = []
        for i in result["skins"]:
            res.append(i["id"])
        return(res)

    def get_champion_skin_number(self, champion_id):
        result = self.data_dao.find_item("DATA", "CHAMPION", "id", champion_id)
        res = []
        for i in result["skins"]:
            res.append(str(i["num"]))
        return(res)
        
    def find_champion_loading_images_by_skin_number(self, skin_number):
        result = self.data_dao.find_item("IMG", "LOADING", "champion_skin_number", skin_number)
        return result



    def insert_champion_loading_skin(self, input_data):
        result = self.data_dao.find_item("IMG", "LOADING", "champion_skin_number", input_data['champion_skin_number'])
        if result is None:
            result = self.data_dao.insert_item("IMG", "LOADING", input_data)
        return result

    def get_champion_loading_skin(self, champion_skin_number):
        result = self.data_dao.find_item("IMG", "LOADING", 'champion_skin_number', champion_skin_number)
        return result
           
           
    def find_champion_splash_images_by_skin_number(self, skin_number):
        result = self.data_dao.find_item("IMG", "SPLASH", "champion_skin_number", skin_number)
        return result

    def insert_champion_splash_skin(self, input_data):
        result = self.data_dao.find_item("IMG", "SPLASH", "champion_skin_number", input_data['champion_skin_number'])
        if result is None:
            result = self.data_dao.insert_item("IMG", "SPLASH", input_data)
        return result

    def get_champion_splash_skin(self, champion_skin_number):
        result = self.data_dao.find_item("IMG", "SPLASH", 'champion_skin_number', champion_skin_number)
        return result

    def insert_champion_square_image(self, input_data):
        result = self.data_dao.find_item("IMG", "SQAURE", "champion_name", input_data['champion_name'])
        if result is None:
            result = self.data_dao.insert_item("IMG", "SQUARE", input_data)
        return result

    def get_champion_square_image(self, champion_id):
        result = self.data_dao.find_item("IMG", "SQUARE", 'champion_name', champion_id)
        return result

    def find_champion_square_image_by_champion_id(self, champion_id):
        result = self.data_dao.find_item("IMG", "SQAURE", "champion_name", champion_id)
        return result

    def insert_champion_spell_images(self, input_data):
        result = self.data_dao.find_item("IMG", "SPELLS", "champion_id", input_data['champion_id'])
        if result is None:
            # temp = {}
            # temp['champion_id'] = input_data['champion_id']
            # temp['spell_id_list'] = input_data['spell_id_list']
            # temp['P'] = ""
            # temp['Q'] = ""
            # temp['W'] = ""
            # temp['E'] = ""
            # temp['R'] = ""
            # result = self.data_dao.insert_item("IMG", "SPELLS", temp)
            # self.data_dao.update_item("champion_id", input_data['champion_id'], "P", input_data['P'], "IMG", "SPELLS")
            # def update_item(self, column_name, column_value, update_column, update_value, db_name, collection_name):
            # self.data_dao.update_row("champion_id", input_data['champion_id'], input_data, "IMG", "SPELLS")
            return result
            
        return result

    def get_champion_spell_images_by_champion_id(self, champion_id):
        result = self.data_dao.find_item("IMG", "SPELLS", 'champion_id', champion_id)
        return result

    def find_champion_spell_images_by_champion_id(self, champion_id):
        result = self.data_dao.find_item("IMG", "SPELLS", 'champion_id', champion_id)
        return result 