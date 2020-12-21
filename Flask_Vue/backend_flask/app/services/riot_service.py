import sys
import os
import base64
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../../mongodb")
from MongoDBHandler import MongoDBHandler
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../../RiotAPI")
from WatcherHandler import WatcherHandler

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../../mongodb/services")
from data_service import DataService
    

class RiotService:
    def __init__(self):
        self.dbHandler = MongoDBHandler()
        self.apiHandler = WatcherHandler()
        print("라우트핸들러 생성")

    @classmethod
    def init_playerinfo_by_name(self, name):
        self.dbHandler = MongoDBHandler()
        self.apiHandler = WatcherHandler.init_by_name(name)
        if (self.apiHandler != None):
            print("클래스라우터핸들러 생성")
            return self()
        else:
            return None
        
    def createSummaryChampions(self):
        api_result = self.apiHandler.test_get_champion_json() 
        # 이후에 해당 챔피언 상세 데이타도 DB에 들어가야함.
        refine = api_result['data']
        name = list(refine.keys())
        for id in name:
            summarychampion = {'id':id, 'name':refine[id]['name'], 'title':refine[id]['title']}
            self.dbHandler.insert_champions_summary(summarychampion)

        #print(list(refine.keys()))
        # print(api_result['data']['Zoe']['name'])
        # print(api_result['data']['Zoe']['title'])
        # print(api_result['name'])

    def countSummaryChampions(self): # SummaryChampions document가 비어있는지 확인
        cnt = self.dbHandler.count_document("DATA", "CHAMPIONS_SUMMARY")
        return cnt

    def getSummaryChampions(self):
        return self.dbHandler.get_champions_summary()

    def searchPlayerInfo(self, name):
        #print(self.apiHandler.test_get_summoner_info_by_account()) #이상

        #print(self.apiHandler.test_get_summoner_info_by_name(name))

        #print(self.apiHandler.test_get_summoner_info_by_puuid()) # 이상

        #print(self.apiHandler.test_get_summoner_info_by_id())

        api_result = self.apiHandler.test_get_summoner_info_by_name(name)
        db_result = self.dbHandler.find_playerInfo_by_name(api_result["name"])
        if db_result is None: # DB에 들어가있지 않은 상태
            self.dbHandler.insert_playerInfo(api_result)
            print("검색한 Player의 DB 추가")
        elif api_result["revisionDate"] != db_result["revisionDate"]:
            self.dbHandler.update_player(db_result["name"], api_result)
            print("검색한 Player의 DB 갱신")
        db_result = self.dbHandler.find_playerInfo_by_name(api_result["name"])
        db_result.pop('_id')
        return db_result

    def createChampioninfoData(self):
        api_result = self.apiHandler.test_get_champion_json() 
        refine = api_result['data']
        name = list(refine.keys())
        for id in name:
            championInfoData = self.apiHandler.test_get_champion_data_by_champion_id(id)
            result = championInfoData['data'][id]
            result.pop('recommended')
            self.dbHandler.insert_champion_data(result)


    def getChampioninfoData(self, champion_name):
        # createChampioninfoData 함수가 반드시 호출 된 이후에 호출 된다.(검사 여기서 안함)
        db_result = self.dbHandler.find_item("DATA", "CHAMPION", "id", champion_name)
        result = []
        result.append(self.getChampioninfo_ChampionInfo(db_result))
        result.append(db_result['stats'])
        result.append(self.getChampioninfo_Spellname(db_result))
        result.append(self.getChampioninfo_Spellcontent(db_result))
        return result

    def getChampioninfo_ChampionInfo(self, result):
        champion_info = []
        champion_info.append(result['name'])
        champion_info.append(result['title'])
        binary_image = self.get_square_image_by_champion_id(result['id'])['img']
        payload= base64.b64encode(binary_image).decode('utf-8')
        champion_info.append(payload) # DB에 이미지 파일이 있다고 가정 하면 경로가 바뀌어야함.
        champion_info.append(result['tags'])
        champion_info.append(result['info'])
        champion_info.append(result['skins'])
        return champion_info

    def getChampioninfo_Spellname(self, result):
        spell_info = []
        spell_info.append(result['passive']['name'])
        spell_info.append(result['spells'][0]['name'])
        spell_info.append(result['spells'][1]['name'])
        spell_info.append(result['spells'][2]['name'])
        spell_info.append(result['spells'][3]['name'])
        return spell_info

    def getChampioninfo_Spellcontent(self, result):
        spell_content = []
        spell_content.append(result['passive']['description'])
        spell_content.append(result['spells'][0]['tooltip'])
        spell_content.append(result['spells'][1]['tooltip'])
        spell_content.append(result['spells'][2]['tooltip'])
        spell_content.append(result['spells'][3]['tooltip'])
        return spell_content

    def testFunction(self, champion_skin_id):
        api_result = self.apiHandler.test_get_champion_loading_img_by_champion_skin_id(champion_skin_id)
    
    def insert_loading_image_by_champion_skin_id(self, champion_name, champion_skin_id):
        api_result = self.apiHandler.test_get_champion_loading_img_by_champion_skin_id(champion_skin_id)
        inputdata = {'chmapion_name' : champion_name, 'champion_skin_id':champion_skin_id, 'img':api_result.content}
        db_result = self.dbHandler.insert_champion_loading_skin(inputdata)
        return db_result

    def get_loading_image_by_champion_skin_id(self, champion_skin_id):
        db_result = self.dbHandler.get_champion_loading_skin(champion_skin_id)
        return db_result

    def create_splash_images(self):
        # db_result = self.dbHandler.get_champion_skin_ids("Zoe")
        champion_id_list = self.dbHandler.get_champion_ids()
        for champion_id in champion_id_list:
            champion_skin_numbers = self.dbHandler.get_champion_skin_number(champion_id)
            for chmapion_skin_number in champion_skin_numbers:
                skin_numbering = champion_id + "_" + chmapion_skin_number
                self.insert_splash_image_by_champion_skin_number(champion_id, skin_numbering)

    def insert_splash_image_by_champion_skin_number(self, champion_name, champion_skin_number):
        if self.dbHandler.find_champion_splash_images_by_skin_number(champion_skin_number) is None:
            api_result = self.apiHandler.test_get_champion_splash_img_by_champion_skin_number(champion_skin_number)
            inputdata = {'chmapion_name' : champion_name, 'champion_skin_number':champion_skin_number, 'img':api_result.content}
            db_result = self.dbHandler.insert_champion_splash_skin(inputdata)

    def find_champion_splash_images_by_skin_number(self, champion_skin_number):
        db_result = self.dbHandler.find_champion_splash_images_by_skin_id(champion_skin_number)
        return db_result

    def get_splash_image_by_champion_skin_id(self, champion_skin_id):
        db_result = self.dbHandler.get_champion_splash_skin(champion_skin_id)
        return db_result

    def count_splash_champion_image(self):
        cnt = self.dbHandler.count_document("IMG", "SPLASH")
        return cnt

    def create_square_images(self):
        champion_id_list = self.dbHandler.get_champion_ids()
        for champion_id in champion_id_list:
            self.insert_square_image_by_champion_id(champion_id)

    def insert_square_image_by_champion_id(self, champion_id):
        if self.dbHandler.find_champion_square_image_by_champion_id(champion_id) is None:
            api_result = self.apiHandler.test_get_champion_square_img_by_champion_id(champion_id)
            inputdata = {'champion_name' : champion_id, 'img':api_result.content}
            db_result = self.dbHandler.insert_champion_square_image(inputdata)

    def find_champion_square_image_by_champion_id(self, champion_id):
        db_result = self.dbHandler.find_champion_square_image_by_champion_id(champion_skin_number)
        return db_result

    def get_square_image_by_champion_id(self, champion_id):
        db_result = self.dbHandler.get_champion_square_image(champion_id)
        return db_result

    def count_square_champion_image(self):
        cnt = self.dbHandler.count_document("IMG", "SQAURE")
        return cnt
        

    def create_champion_spell_images(self):
        champion_id_list = self.dbHandler.get_champion_ids()
        for champion_id in champion_id_list:
            self.insert_spell_images_by_champion_id(champion_id)

    def insert_spell_images_by_champion_id(self, champion_id):
        db_result = self.dbHandler.find_item("DATA", "CHAMPION", "id", champion_id)
        if self.dbHandler.find_champion_spell_images_by_champion_id(champion_id) is None:
            spell_id_list = []
            P = db_result['passive']['image']['full']
            Q = db_result['spells'][0]['image']['full']
            W = db_result['spells'][1]['image']['full']
            E = db_result['spells'][2]['image']['full']
            R = db_result['spells'][3]['image']['full']
            spell_id_list.append(P)
            spell_id_list.append(Q)
            spell_id_list.append(W)
            spell_id_list.append(E)
            spell_id_list.append(R)

            inputdata = {}
            inputdata['champion_id'] = champion_id
            inputdata['spell_id_list'] = spell_id_list
            inputdata['P'] = self.apiHandler.test_get_champion_passive_img_by_champion_passive_id(P)
            inputdata['Q'] = self.apiHandler.test_get_champion_spell_img_by_champion_spell_id(Q)
            inputdata['W'] = self.apiHandler.test_get_champion_spell_img_by_champion_spell_id(W)
            inputdata['E'] = self.apiHandler.test_get_champion_spell_img_by_champion_spell_id(E)
            inputdata['R'] = self.apiHandler.test_get_champion_spell_img_by_champion_spell_id(R)
            db_result = self.dbHandler.insert_champion_spell_images(inputdata)

    def find_champion_spell_images_by_champion_id(self, champion_id):
        db_result = self.dbHandler.find_champion_spell_images_by_champion_id(champion_id)
        return db_result

    def get_champion_spell_images_by_champion_id(self, champion_id):
        db_result = self.dbHandler.get_champion_spell_images_by_champion_id(champion_id)
        return db_result

    def count_spell_champion_image(self):
        cnt = self.dbHandler.count_document("IMG2", "SPELLS")
        return cnt

    def testFunction(self, champion_id):
        api_result = self.apiHandler.test_get_champion_loading_img_by_champion_skin_number(champion_skin_id)