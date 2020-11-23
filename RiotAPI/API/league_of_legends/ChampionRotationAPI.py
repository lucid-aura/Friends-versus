import re

from ..BaseAPI import BaseAPI
from ..NamedEndpoint import NamedEndpoint
from .LeagueEndpoint import LeagueEndpoint




class ChampionRotationUrls:
    rotations = LeagueEndpoint("/platform/v3/champion-rotations")


class ChampionRotationAPI(NamedEndpoint):
    def __init__(self, base_api: BaseAPI):
        super().__init__(base_api, self.__class__.__name__)
    
    def rotations(self, region: str):
        return self._request_endpoint(
            self.rotations.__name__, region, ChampionRotationUrls.rotations
        )