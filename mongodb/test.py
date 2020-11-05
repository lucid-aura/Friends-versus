# https://basketdeveloper.tistory.com/34
from pymongo import MongoClient 

MONGODB_HOST = '0.0.0.0'
MONGODB_PORT = 27017

client = MongoClient(host=MONGODB_HOST,
                    port=MONGODB_PORT)

db = client['test']
print(db)