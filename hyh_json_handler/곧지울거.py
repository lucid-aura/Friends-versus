import time
import datetime

## importing socket module 내 localhost 확인하기
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# try:
#     # doesn't even have to be reachable
#     s.connect(('10.255.255.255', 1))
#     IP = s.getsockname()[0]
# except:
#     IP = '127.0.0.1'
# finally:
#     s.close()
# print(IP)
# print(socket.gethostbyname(socket.gethostname()))


# a = int(round(time.time() * 1000))
# print(a)
# b = datetime.datetime.fromtimestamp(1606613151000/1000.0, tz=datetime.timezone.utc)
# print(b)
# c = datetime.datetime.fromtimestamp(1606613151000/1000.0)
# print(c)

# # 이미지를 mongoDB에 미리 저장을 해놔야 하는가?????
# #  RiotApi를 통해 이미지도 얻을 수 있는가?

# a = {'a':'a', 'b':'b', 'c':'c'}
# k = a.items
# print(list(a.keys()))






# ## RiotAPI - mongoDB  연동
# #### RiotAPI - WactherHandler.py
# - 기존의 테스트 파라미터에서 입력값으로 변경
# - 닉네임으로 플레이어 정보를 얻어오는 함수 추가
# - API 요청 반환값은 Json

# #### mongoDB - MongoDBHandler.py
# - MongoDBHandler class를 정의
# - 기존의 test Handler를 MongoDBHandler로 통합
# - row를 업데이트 하는 update_row 함수 추가
# - player를 업데이트하는 update_player 함수 추가
# - player의 정보를 추가하는 insert_playerInfo 함수 추가
# - player 이름을 검색하여 playerInfo를 반환하는 find_playerInfo_by_name 함수 추가

# ## Flask - RiotAPI/mongoDB 연동
# #### Flask - routeHandler.py
#  - MongoDBHandler class 와 WatcherHandler class를 이용하여 Flask route 제어
# ```
# RouteHandler - searchPlayerInfo
# - player name을 입력받아 해당 이름을 가지는 API결과와 DB 조회 결과를 가진다.
# ```
# ## Flask - Vue 연동
# #### Flask - route.py
# - Vue에서 요청하는 라우터에서의 동작을 정의
# - 모든 데이터의 접근과 통제는 routeHandler class 에서 이루어져야 한다.
# ```
# route('/') root(home)
# - root(home) 에서는 플레이어 이름을 입력받아 해당 플레이어의 정보를 json 형태로 반환.
# - player DB에 revisionTime은 miliseconds로 되어있으므로 datetime 형태로 변환
# ```

# #### Vue - Home.vue
# - 사이트 접근 시 가장먼저 보여주는 root page 
# - 플레이어 닉네임을 입력하는 playerinfo input이 있다.
# - 닉네임 입력 시 http://localhost:5000/?playerinfo 로 GET 요청을 한다.
# - 요청 결과를 자식 컴포넌트인 PlayerInfo.vue에 전달한다.

# #### Vue - PlayerInfo.vue
# - 검색된 플레이어 정보를 보여주는 vue
# - profileIcon, name, summonerLevel, revisionDate 값을 table에 뿌린다.
