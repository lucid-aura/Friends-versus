import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../../mongodb")
from MongoDBHandler import MongoDBHandler
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../../RiotAPI")
from WatcherHandler import WatcherHandler
    

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

        # for index in db_result:
        #     print(index)
            # api_result = self.apiHandler.test_get_champion_data_by_champion_id(index['id']) 
            # print(api_result)
            # refine = api_result
            # refine.pop('recommended')
            # result = self.dbHandler.insert_item("CHAMPION", "DATA", refine)
            # print(refine)
            
        


    def getChampioninfoData(self, champion_name):
        # 데이터를 api로 요청해서 가지고 오는 것과 DB에 저장해서 가지고 오는 것 둘다 구현해야 할 것 같다.
        # api_result = self.apiHandler.test_get_champion_data_by_champion_id(champion_name)
        # raw_result = api_result['data'][champion_name]
        # result = raw_result.pop('recommended') # 지금은 필요없는 데이터(추천) 삭제

        # db에 넣기.. 이후에 제거 or 수정해줘야함. 한번만 넣고 변동사항있을때만 변경
        # db_result = self.dbHandler.insert_item("CHAMPION", "DATA", inputtest) #

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
        champion_info.append(result['image']['full']) # DB에 이미지 파일이 있다고 가정 하면 경로가 바뀌어야함.
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