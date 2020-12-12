docker-compose 를 사용해 mongodb, mongodb-express

## docker-compose.yml
- 도커 이미지 : mongoDB(0.0.0.0:27017)
- 도커 이미지 : mongo-express(0.0.0.0:8081)
- 도커 볼륨 : mongodb ( /data/db 와 매핑 ) 

## 실행 커맨드
~~~sh
docker-compose up -d 
docker-compose down
~~~

## 연결 테스트 커맨드
~~~sh
pip install pymongo
python test
~~~


## MongoDBHandler.py
- __init__ 는 인스턴스가 초기화 될 떄 불러와지는 형태

- insert_item(self, db_name, collection_name, input_data)
-- DB, collection 이름에 해당하는 DB에 input_data 삽입
-- input_data는 JSON 파일 포맷

- inserts_item(self, db_name, collection_name, input_data)
-- DB, collection 이름에 해당하는 DB에 input_data 삽입
-- input_data는 JSON 파일 포맷의 list

- find_item(self, db_name, collection_name, column_name, column_value)
-- DB, collection 이름에 해당하는 DB에 column_name 열에 column_value가 있는지 조회
-- 해당 데이터가 있으면 해당 row를 dict 형태로 반환
-- 해당 데이터가 없으면 None 반환

- find_items(self, db_name, collection_name, column_name, column_value)
-- DB, collection 이름에 해당하는 DB에 column_name 열에 column_value가 있는지 조회
-- 해당 데이터가 있으면 해당 row를 dict 형태의 list로 반환
-- 해당 데이터가 없으면 None 반환

- delete_item(self, column_name, column_value, db_name, collection_name)
-- DB, collection 이름에 해당하는 DB에 column_name 열에 column_value가 있는지 조회하여 결과가 있으면 해당 row 삭제
-- 삭제 결과를 반환

- update_item(self, column_name, column_value, update_column, update_value, db_name, collection_name)
-- DB, collection 이름에 해당하는 DB에 column_name 열에 column_value가 있는지 조회하여 결과가 있으면 update_column의 value를 update_value로 갱신.
-- 갱신 결과를 반환

- update_row(self, column_name, column_value, update_values , db_name, collection_name)
-- update_values는 딕셔너리 형태
-- DB, collection 이름에 해당하는 DB에 column_name 열에 column_value가 있는지 조회하여 결과가 있으면 update_values의 values로 값들을 갱신

- count_document(self, db_name, collection_name)
-- DB, collection 이름에 해당하는 document가 가지고있는 원소의 개수 반환

- update_player(self, name, update_values)
-- 이름과 일치하는 소환사의 정보를 update_values로 업데이트 함.
-- update_values는 dict 형태

- create_condition(self, column_name, column_value)
-- column_name 과 column_value의 쌍을 이루는 str 형태의 dict 반환

- insert_playerInfo(self, playerInfo)
-- playerInfo를 데이터베이스에 저장
-- playerInfo는 JSON 형태

- insert_champions_summary(self, champion_summary)
-- insert_champions_summary 데이터베이스에 저장
-- insert_champions_summary JSON 형태

- get_champions_summary(self)
-- CHAMPIONS_SUMMARY document에 있는 챔피언 요약정보( {name : title} )를 JSON 형태로 반환

- insert_champion_data(self, champion_data)
-- 해당 챔피언 정보가 아직 DB에 없다면 그 챔피언 데이터를 DB에 저장

- get_champion_data(self, champion_id)
-- champion_id 에 해당하는 챔피언을 dict 형식으로 반환

- find_playerInfo_by_name(self, name)
-- name을 가지는 플레이어 정보를 DB에서 조회하여 dict 형태로 반환


- insert_champion_loading_skin(self, input_data):
-- input_data의 champion_skin_id 값을 가지는 LOADING 이미지를 [IMG][LOADING] DB에 추가


- get_champion_loading_skin(self, champion_skin_id):
-- champion_skin_id 의 값을 가지는 이미지를 [IMG][LOADING] DB에서 조회하여 로드

            
## 참고자료
- https://m.blog.naver.com/wideeyed/221974024860
