import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../mongodb")
from MongoDBHandler import MongoDBHandler
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../RiotAPI")
from WatcherHandler import WatcherHandler


host='192.168.40.52'
port=27017
username='root'
password='root12345!'

class RouteHandler:
    def __init__(self):
        self.dbHandler = MongoDBHandler(host, port, username, password)
        self.apiHandler = WatcherHandler()
        print("라우트핸들러 생성")

    @classmethod
    def init_by_name(self, name):
        self.dbHandler = MongoDBHandler(host, port, username, password)
        self.apiHandler = WatcherHandler.init_by_name(name)
        print("클래스라우터핸들러 생성")
        return self()
        

    def searchPlayerInfo(self, name):
        #print(self.dbHandler.insert_playerInfo(self.apiHandler.test_get_summoner_info_by_name(name)))
        # name = "가 짜"
        # db_result = self.dbHandler.find_playerInfo_by_name(name)
        # print(db_result)
        # return self.apiHandler.test_get_summoner_info_by_name(name)

        #print(self.apiHandler.test_get_summoner_info_by_account()) #이상

        #print(self.apiHandler.test_get_summoner_info_by_name(name))

        #print(self.apiHandler.test_get_summoner_info_by_puuid()) # 이상

        #print(self.apiHandler.test_get_summoner_info_by_id()) 
        api_result = self.apiHandler.test_get_summoner_info_by_name(name)
        db_result = self.dbHandler.find_playerInfo_by_name(api_result["name"])
        if db_result[0] is None: # DB에 들어가있지 않은 상태
            self.dbHandler.insert_playerInfo(api_result)
            print("검색한 Player의 DB 추가")
        elif api_result["revisionDate"] != db_result[0]["revisionDate"]:
            self.dbHandler.update_player(db_result[0]["name"], api_result)
            print("검색한 Player의 DB 갱신")
        #print(db_result[0]["name"])
        return api_result
        