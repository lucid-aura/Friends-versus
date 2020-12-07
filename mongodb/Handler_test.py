from db_handler import MongoDBHandler
from config import JsonConfig

import pymongo
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/hyh_json_handler")
from JsonParser import JsonParser

#host='192.168.200.163'
host='192.168.40.52'
host='192.168.40.64'
port=27017
username='root'
password='root12345!'

test = MongoDBHandler(host, port, username, password)
develop_json = JsonConfig("Develop.json") # Develope Json 파일 열고 로드

temp_stat = {"id":"Aaatrox", "hp":580,"hpperlevel":90,"mp":0,"mpperlevel":0,"movespeed":345,"armor":38,"armorperlevel":3.25,"spellblock":32.1,"spellblockperlevel":1.25,"attackrange":175,"hpregen":3,"hpregenperlevel":1,"mpregen":0,"mpregenperlevel":0,"crit":0,"critperlevel":0,"attackdamage":60,"attackdamageperlevel":5,"attackspeedperlevel":2.5,"attackspeed":0.651}
#중복 방지 확인용 임시 테스트 데이터 (id : Aatrox -> Aaatrox)

player_json_path = develop_json.config["DATA"]["PLAYER"]
player_json = JsonConfig(player_json_path) # Develop.json에서 얻은 경로로 player.json 파일 로드
#player_data = champion_json.config["data"] #PlayerDB에서 data collection 로드

# get a latest champion status info form champion.json
# champion_json_path = develop_json.config["DATA"]["CHAMPIONSTAT"] #로드 된 json 파일에서 champion json 찾음.
# champion_json = JsonConfig(champion_json_path)
# champion_data = champion_json.config["data"] # championDB에서 data collection 로드
# champion_parser = JsonParser(champion_data)
# parsing = champion_parser.parsing_champion_data()

#test.insert_items("Champion", "Champion_stat", parsing)


#champion_data = Jsonparser(json_parser)
#print(champion_data.parsing_data())
#test.insert_items("Champion", "Champion_stat", champion_data)
#test.check_duplicate("Champion", "Champion_stat", "id") #Champion.champion_stat의 id에 unique_index 생성 (중복 방지)
#test.insert_item("Champion", "Champion_stat", temp_stat) # 중복되면 에러 발생.
#1개 insert는 딕셔너리 타입 / 다수 개 insert는 딕셔너리를 원소로 갖는 list 타입으로 넘김.

# find function test
# find1 = test.find_item("id", "Zoe", "Champion", "Champion_stat") # 검색 기능 확인 1. Zoe 챔피언의 스탯 정보
# print(find1)
# find2 = test.find_items("Champion", "Champion_stat", "id") # 검색 기능 확인 2. 테이블의 모든 id (챔피언 이름) 정보
# print(find2)


# get a latest version info from version.json
version_json_path = develop_json.config["DATA"]["VERSION"]
version_json = JsonConfig(version_json_path)
version_parser = JsonParser(version_json.config)
version = version_parser.client_version()

# version check
version_in_db = test.find_items("Version", "Version", "version") # 버전은 한가지만 존재 (list의 첫번째)
if len(version_in_db) == 0: # initalize version(insert version info)
    test.insert_item("Version", "Version", {"version": version})
elif version_in_db[0] != version: # update version
    test.update_item("version", version_in_db[0], "version", version, "Version", "Version")
    print("need to update data") # api 통해 데이터 새로 받아와야함. (갱신 필요)
else: # aleady latest version
    print("version is latest :" + version_in_db[0] )

