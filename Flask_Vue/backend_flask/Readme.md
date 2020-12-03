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
run.py
config.py
.flaskenv
requirements.txt
~~~
## Configuration
`config.py`에서 
## 애플리케이션 세팅
`app/__init__.py`에서 앱 인스턴스 생성과 라우트를 임포트한다
## 프로젝트 라우트
`app/routes.py`에서 모든 라우트와 웹 애플리케이션의 백엔드 로직을 정함