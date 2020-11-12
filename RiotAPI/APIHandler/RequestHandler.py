from abc import *

class RequestHandler(metaclass=ABCMeta):

    @abstractmethod
    def preview_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        query_params: dict):
        pass 

    @abstractmethod
    def after_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        response):
        pass 

    @abstractmethod
    def preview_static_request(
        self,
        url: str,
        query_params: dict):
        pass

    @abstractmethod
    def after_static_request(
        self,
        url: str,
        response):
        pass 