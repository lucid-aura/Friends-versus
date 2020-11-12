# https://basketdeveloper.tistory.com/34
from pymongo import MongoClient 

MONGODB_HOST = 'host.docker.internal'
MONGODB_PORT = 27017

client = MongoClient(host=MONGODB_HOST,
                    port=MONGODB_PORT, username='root', password='root12345!',)

db = client['test2']
print(db)
col = db['document2']

x = col.insert_one({"name":"Songhyun", "gender":"female"}) 
print(x.inserted_id)