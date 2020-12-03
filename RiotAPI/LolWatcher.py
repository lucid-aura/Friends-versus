from API.BaseAPI import BaseAPI

from API.league_of_legends import (
    SummonerAPI,
    DataDragonAPI,
    ChampionRotationAPI,
    ChampionMasteryAPI
)
# from API.league_of_legends import (ChampionMasteryAPI)
from Handler.RequestHandler import RequestHandler
from Handler import (
    Deserializer,
    DeserializerAdapter,
    DictionaryDeserializer
)


# remote riotAPI Server -   SummonerAPI       | Web |      SummonerAPI.py   - LolWatcher.py - 우리 
#                       -   ChampionAPI       |     |      ChampionAPI.py   -

from pprint import pprint 
import json 


class LolWatcher:
    def __init__(self, api_key: str, timeout: int = None, deserialier: Deserializer = DictionaryDeserializer):
        """
        RiotWatcher 클래스 객체 초기화
        :param string api_key
        :param int timeout: time to wait for response
        """
        if not api_key:
            raise ValueError("api_key must be set!")

        # handler_chain = [ DeserializerAdapter.DeserializerAdapter(deserialier),]
        #self._base_api = BaseAPI(api_key, handler_chain)
        
        self._base_api = BaseAPI(api_key)

        self._datadragon = DataDragonAPI.DataDragonAPI(self._base_api)
        self._summoner = SummonerAPI.SummonerAPI(self._base_api)
        self._championrotation = ChampionRotationAPI.ChampionRotationAPI(self._base_api)
        self._championmastery = ChampionMasteryAPI.ChampionMasteryAPI(self._base_api)
        
    @property
    def datadragon(self):
        return self._datadragon

    @property
    def summoner(self):
        return self._summoner

    @property
    def championrotation(self):
        return self._championrotation

    @property
    def championmastery(self):
        return self._championmastery