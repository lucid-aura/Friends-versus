import requests

class BaseAPI:
    def __init__(self, api_key, request_handlers=None, time_out=None):
        # protected -> 접두사에 _ 을 적용
        # private -> 접두사에 __ 을 적용
        self._api_key = api_key
        self._request_handlers = request_handlers
        self.time_out = time_out

    # 파이썬에서는 @property 데코레이터를 이용하여 위의 get, set 메소드보다 더욱 직관적으로 표현 가능
    # get의 역할을 property
    # set의 역할을 setter가 한다
    @property
    def api_key(self):
        return self._api_key

    
    def raw_request(self, endpoint_name: str , # 변수의 정적 선언
                method_name: str, 
                region: str,
                url: str,
                query_params: dict) -> Any:
        query_params = {key: val for key, val in query_params.items() if val is not None}
        response = None 
        early_return_index = None 

        



