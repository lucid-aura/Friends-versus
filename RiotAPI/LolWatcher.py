from API.BaseAPI import BaseAPI
from API.league_of_legends.SummonerAPI import SummonerAPI
from API.league_of_legends.DataDragonAPI import DataDragonAPI

from Handler.RequestHandler import RequestHandler
from Handler import (
    Deserializer,
    DeserializerAdapter,
    DictionaryDeserializer
)

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

        self._datadragon = DataDragonAPI(self._base_api)
        self._summoner = SummonerAPI(self._base_api)
        
        @property
        def datadragon(self):
            return self._datadragon

        @property
        def summoner(self):
            return self._summoner

if __name__ == "__main__":
    lol_watcher = LolWatcher("RGAPI-330711e3-2f76-48c1-b832-6a455f132270")
    my_region = 'kr'

    lol_versions = lol_watcher._datadragon.versions_for_region(my_region)
    lol_versions_json = json.loads(lol_versions.text)

    pprint(lol_versions_json)
    locale = lol_versions_json['l']
    champion_version = lol_versions_json['n']['champion']

    lol_champions = lol_watcher._datadragon.champions(version=champion_version, full=False, locale='')
    pprint(json.loads(lol_champions.text))

    #my_ranked_stats = lol_watcher._summoner.by_name(my_region, "휘랑")
    #print(my_ranked_stats.text)
