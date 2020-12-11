## Flask
Python Simple Backend Server, ( Django )
우리 시스템에서의 역할 
- Vue.js 로드
- MongoDB 컨트롤
- RiotAPI 컨트롤


Vue.js(route : /index) -> Flask( /index) -> MongoDB ( Data Input )     
Vue.js -> Flask -> MongoDB -> Flask -> Vue.js (Refresh)( Data 조회 )

마크다운 형식...으로 작성하고 있는건데

## 프로젝트 구조
~~~
app 
ㄴ __init__.py
ㄴ routes.py
ㄴ routeHandler.py
run.py
config.py
.flaskenv
requirements.txt
~~~
## Configuration
`config/config.py - FlaskConfig`에서 
## 애플리케이션 세팅
`app/__init__.py`에서 앱 인스턴스 생성과 라우트를 임포트한다
## 프로젝트 라우트
`app/routes.py`에서 모든 라우트와 웹 애플리케이션의 백엔드 로직을 정함
`app/RouteHandler.py`에서 routes.py에 쓰이는 함수들을 정의

## 함수 정리

### routes.py

### RouteHandler.py
- __init__(self):
-- MongoDBHandler와 WatcherHandler를 가지는 RouteHandler 생성

- init_playerinfo_by_name(self, name)
-- MongoDBHandler와 소환사 이름을 입력한 WatcherHandler를 가지는 RouteHandler 생성
        
- createSummaryChampions(self):
-- RiotAPI를 조회하여 id와 name 값을 가지는 CHAMPIONS_SUMMARY document 생성
-- 최초 생성 시, 버전업에 따른 새로운 챔피언 출시 그리고 이름이나 타이틀이 바뀌는 챔피언이 있을 시 갱신 함수 필요

- countSummaryChampions(self): 
-- CHAMPIONS_SUMMARY document에 들어있는 원소 개수 확인
-- 최초 생성을 확인하거나 새로운 챔피언 추가시 업데이트를 위한 함수

- getSummaryChampions(self):
-- CHAMPIONS_SUMMARY에 모든 원소들을 가져오는 함수
-- ChampionList.vue에서 보여줄 값들을 위해 사용된다. 

- searchPlayerInfo(self, name):
-- Home.vue 에서 조회한 닉네임을 RiotAPI로 조회하고 실재 있는 닉네임이면 DB에서 확인 후 DB에 추가 및 반환

- createChampioninfoData(self):
-- 챔피언의 세부사항 data가 담긴 JSON을 RiotAPI에 요청하여 넣고 recommended를 빼서 DB에 넣는다.

- getChampioninfoData(self, champion_name):
-- 챔피언이름.json에서 챔피언 설명, 스탯, 스킬이름, 스킬 설명을 가져온다.
-- ChampionInfo.vue 에 출력 될 내용을 정리하여 return 한다.

- getChampioninfo_ChampionInfo(self, result):
-- 챔피언 기본 정보를 리스트로 반환한다.

- getChampioninfo_Spellname(self, result):
-- 챔피언 스킬 이름를 리스트로 반환한다.

- getChampioninfo_Spellcontent(self, result):
-- 챔피언 스킬 정보를 리스트로 반환한다.

- testFunction(self, champion_skin_id):
-- 테스트 함수

- get_loading_image_by_champion_skin_id(self, champion_skin_id):
-- 로딩 화면에서의 챔피언 이미지를 DB에서 가지고 온다.
-- 현재 itemlist.vue 에서 확인 가능.

## 추가 사항
- Champion_summury 와 Champion_info 생성은 동시에 진행해도 될 것 같다.