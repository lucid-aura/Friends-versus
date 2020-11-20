import re 

from ..BaseAPI import BaseAPI
from ..NamedEndpoint import NamedEndpoint
from ..Endpoint import Endpoint

class DataDragonEndpoint(Endpoint):
    def __init__(self, url, **kwargs):
        nurl = f"https://ddragon.leagueoflegends.com{url}"
        super().__init__(nurl, **kwargs)

class DataDragonVersionLocaleEndpoint(DataDragonEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/cdn/{{version}}/data/{{locale}}{url}"
        super().__init__(nurl, **kwargs)

class DataDragonUrls:
    versions = DataDragonEndpoint("/realms/{region}.json")
    championsFull = DataDragonVersionLocaleEndpoint("/championFull.json")
    champions = DataDragonVersionLocaleEndpoint("/champion.json")

class DataDragonAPI:
    def __init__(self, base_api: BaseAPI):
        self._base_api = base_api

    def _request(self, endpoint: Endpoint, version: str, locale: str):
        url, query = endpoint(version=version, locale=locale if locale else "en_US")
        return self._base_api.raw_request_static(url, query)

    def versions_for_region(self, region: str):
        region = re.sub(r"\d", "", region)
        url, query = DataDragonUrls.versions(region=region)
        return self._base_api.raw_request_static(url, query)

    def champions(self, version: str, full: bool = False, locale=None):
        return self._request(
            DataDragonUrls.championsFull if full else DataDragonUrls.champions,
            version,
            locale,
        )
    