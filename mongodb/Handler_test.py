from db_handler import MongoDBHandler
from config import JsonConfig
host='192.168.40.52'
port=27017
username='root'
password='root12345!'

test = MongoDBHandler(host, port, username, password)

temp_stat = {"id":"Aatrox", "hp":580,"hpperlevel":90,"mp":0,"mpperlevel":0,"movespeed":345,"armor":38,"armorperlevel":3.25,"spellblock":32.1,"spellblockperlevel":1.25,"attackrange":175,"hpregen":3,"hpregenperlevel":1,"mpregen":0,"mpregenperlevel":0,"crit":0,"critperlevel":0,"attackdamage":60,"attackdamageperlevel":5,"attackspeedperlevel":2.5,"attackspeed":0.651}
#중복 방지 확인용 임시 테스트 데이터

#test.check_version()
champion_json = JsonConfig()
champion_data = champion_json.parsing_champion_data()
test.insert_items("Champion", "Champion_stat", champion_data)
test.check_duplicate("Champion", "Champion_stat", "id") #Champion.champion_stat의 id에 unique_index 생성 (중복 방지)
#test.insert_item("Champion", "Champion_stat", temp_stat) # 중복되면 에러 발생.
#1개 insert는 딕셔너리 타입 / 다수 개 insert는 딕셔너리를 원소로 갖는 list 타입으로 넘김.




test.find_item("id", "Zoe", "Champion", "Champion_stat") # 검색 기능 확인
