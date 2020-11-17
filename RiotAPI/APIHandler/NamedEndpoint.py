from .BaseAPI import BaseAPI
from .Endpoint import Endpoint

class NamedEndpoint:
    """
    헬퍼 클래스다 BaseAPI 객체 호출에 Endpoint의 이름을 주입(inject)하는 방식으로 사용한다. 
    ... 자식 클래스가 이름을 계속 명시적으로 추가하는 방식 대신에 하는 방법이다
    """
    def __init__(self, 
        base_api: BaseAPI, 
        endpoint_name: str):

        print(f"NamedEndpoint -> {endpoint_name}")
        
        """
        새로운 NamedEndpoint를 초기화한다. 미리 준비되어 있는 base_api를 사용한다.
        그리고 _request 가 호출 될 때, endpoint_name을 주입한다. 

        : param base_api : BaseAPI : 모든 request를 만들기 위해 사용하는 루트 APIObject
        : param string endpoint_name : 자식 endpoint의 이름
        """
        self._base_api = base_api
        self._endpoint_name = endpoint_name

    def _request_endpoint(self, 
        method_name: str, 
        region: str, 
        endpoint: Endpoint, 
        **kwargs):
        """
        미리 준비되어 있는 BaseAPI 인스턴스를 통해 request를 보낸다, 
        메소드 호출 했을 때, 미리 준비되어 있는 endpoint_name를 주입해서 

        : param string method_name : 호출하는 메소드 이름
        : param string region : 이 request를 실행하는 region
        : oaram Endpoint endpoint: URL 생성과 파라미터 쿼리를 사용하기 위한 endpoint
        """
        url, query = endpoint(platform=region, **kwargs)
        return self._base_api.raw_request(
            endpoint_name=self._endpoint_name,
            method_name=method_name,
            region=region,
            url=url,
            query_params=query
        )



