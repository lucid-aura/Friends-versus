from pymongo import MongoClient 
import csv

MONGODB_HOST = 'host.docker.internal' # C:\Windows\System32\drivers\etc\hosts 에 저장된 docker Desktop host
MONGODB_PORT = 27017 #MongoDB에서 쓰는 기본 포트
client = MongoClient(host=MONGODB_HOST,
                    port=MONGODB_PORT, username='root', password='root12345!',)

#print("document 이름을 입력해주세요")
#document = input() #document name = Player_info
document = "Player_info"
db = client['test'] # db_name = test
collection = db[document]
COLUMN = ['Player_name','Player_level','Player_icon','Player_tier','Player_win','Player_lose','Player_recent_time'] #Player_info Column

print("수정할 플레이어 이름, 수정할 변수, 수정할 값을 입력해 주세요")
print("ex) Player1 Player_icon 2")
name, var, value = input().split()

f = open(document + '.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

result = collection.find_one( {'Player_name':name})
if result is None:
    print("존재하지 않는 플레이어 이름입니다.")
else:
    query = {"Player_name": name} # target player name
    collection.delete_one(query) # delete target element
    result = collection.find_one({'Player_name': name})
    print(result)

f.close()