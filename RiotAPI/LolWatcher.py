from APIHandler import BaseAPI
from APIHandler.league_of_legends import SummonerAPI

class LolWatcher:
    def __init__(self, api_key: str, timeout: int = None):
        """
        RiotWatcher 클래스 객체 초기화
        :param string api_key
        :param int timeout: time to wait for response
        """
        if not api_key:
            raise ValueError("api_key must be set!")

        self._base_api = BaseAPI.BaseAPI(api_key)
        self._summoner = SummonerAPI.SummonerAPI(self._base_api)

        @property
        def summoner(self):
            return self._summoner

if __name__ == "__main__":
    lol_watcher = LolWatcher("RGAPI-330711e3-2f76-48c1-b832-6a455f132270")
    my_region = 'kr'

    my_ranked_stats = lol_watcher._summoner.by_name(my_region, "휘랑")
    print(my_ranked_stats)
