import requests
from typing import Any


class BaseAPI:
    def __init__(self, api_key, request_handlers=None, timeout=None):
        # protected -> 접두사에 _ 을 적용
        # private -> 접두사에 __ 을 적용
        self._api_key = api_key
        self._request_handlers = request_handlers
        self._timeout = timeout 

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

        if self._request_handlers is not None:
            for idx, handler in enumerate(self._request_handlers, start=1):
                response = handler.preview_request(
                    region,
                    endpoint_name,
                    method_name,
                    url,
                    query_params
                )
                early_return_index = idx
                if response is not None:
                    break   
        if response is None:
            extra = {}
            if self._timeout is not None:
                extra["timeout"] = self._timeout

            response = requests.get(
                url,
                params=query_params,
                headers={"X-Riot-Token": self.api_key},
                **extra
            )
            
        if self._request_handlers is not None:
            for handler in self._request_handlers[early_return_index:None:-1]:
                mod = handler.after_request(
                    region, 
                    endpoint_name, 
                    method_name,
                    url,
                    response 
                )
                if mod is not None:
                    response = mod
        
        return response

    def raw_request_static(self,
        url: str,
        query_params: dict) -> Any:
        query_params = {key: value for key, value in query_params.items() if value is not None} 

        response = None 
        early_ret_idx = None 

        if self._request_handlers is not None:
            for idx, handler in enumerate(self._request_handlers, start=1):
                response = handler.preview_static_request(url, query_params)
                early_ret_idx = idx 
                if response is not None:
                    break 

        if response is None:
            extra = {}
            if self._timeout is not None:
                extra["timeout"] = self._timeout

            response = requests.get(url, params=query_params, **extra)
        
        if self._request_handlers is not None:
            for handler in self._request_handlers[early_ret_idx:None:-1]:
                mod = handler.after_static_request(url, response)
                if mod is not None:
                    response = mod 
        
        return response 


        



