#진행중

from pymongo import MongoClient
import csv

MONGODB_HOST = 'host.docker.internal' # C:\Windows\System32\drivers\etc\hosts 에 저장된 docker Desktop host
MONGODB_PORT = 27017 #MongoDB에서 쓰는 기본 포트
client = MongoClient(host=MONGODB_HOST,
                    port=MONGODB_PORT, username='root', password='root12345!',)

print("document 이름을 입력해주세요")
document = input() #document name = Player_info
db = client['test'] # db_name = test
collection = db[document]
COLUMN = ['Player_name','Player_level','Player_icon','Player_tier','Player_win','Player_lose','Player_recent_time'] # Player_info Column

f = open(document + '.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

for line in lines:
    dict = {name: value for name, value in zip(COLUMN, line)} # make new element
    x = collection.insert_one(dict)
    print(dict)
f.close()