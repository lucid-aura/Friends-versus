# Riot API 관련 개발
## 사용 가능 기능
- CHAMPION-MASTERY-V4
- CHAMPION-V3
- LEAGUE-V4
- MATCH-V4
- SPECTATOR-V4
- SUMMONER-V4

### NamedEndpoint.py

### Endpoint.py
- __init__ 는 인스턴스가 초기화 될 떄 불러와지는 형태
- __call__ 는 인스턴스가 호출 될 때 실행되는 형태이다. 
__call__ 함수를 통해 클래스를 함수로 호출 가능하게 활용하기위해서 사용하는 특수 메소드이다.     
__call__ 함수를 이용해서 객체의 생성 및 종료와 관계없이 객체 내부의 상태를 변경할 수 있게 된다.
### league_of_lengends/SummonerApiV4.py
NamedEndpoint를 상속받아서 사용. 초기화 파라미터로 BaseApi 객체를 넣는다.
[깃헙 참고 아닌 복사본 링크](https://github.com/pseudonym117/Riot-Watcher/blob/master/src/riotwatcher/_apis/league_of_legends/SummonerApiV4.py)

