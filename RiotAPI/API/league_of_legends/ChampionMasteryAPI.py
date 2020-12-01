# Champion-Mastery-V4
from ..BaseAPI import BaseAPI
from ..NamedEndpoint import NamedEndpoint
from .LeagueEndpoint import LeagueEndpoint

class ChampionMasteryEndpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/champion-mastery/v4{url}"
        super().__init__(nurl, **kwargs)

class ChampionMasteryAPIUrls:
    by_summoner = ChampionMasteryEndpoint("/champion-masteries/by-summoner/{encrypted_summoner_id}")
    by_summoner_by_champion = ChampionMasteryEndpoint("/champion-masteries/by-summoner/{encrypted_summoner_id}/by-champion/{champion_id}")
    scores_by_summoner = ChampionMasteryEndpoint("/scores/by-summoner/{encrypted_summoner_id}")

class ChampionMasteryAPI(NamedEndpoint):
    def __init__(self, base_api: BaseAPI):
        super().__init__(base_api, self.__class__.__name__)
    
    def by_summoner(self,
        region: str,
        encrypted_summoner_id: str):

        return self._request_endpoint(
            self.by_summoner.__name__,
            region,
            ChampionMasteryAPIUrls.by_summoner,
            encrypted_summoner_id=encrypted_summoner_id,
        )
    
    def by_summoner_by_champion(self,
        region: str,
        encrypted_summoner_id: str,
        champion_id: int):
        return self._request_endpoint(
            self.by_summoner_by_champion.__name__,
            region,
            ChampionMasteryAPIUrls.by_summoner_by_champion,
            encrypted_summoner_id=encrypted_summoner_id,
            champion_id=champion_id,
        )
    
    def scores_by_summoner(self,
        region: str,
        encrypted_summoner_id: str):
        return self._request_endpoint(
            self.scores_by_summoner.__name__,
            region,
            ChampionMasteryAPIUrls.scores_by_summoner,
            encrypted_summoner_id=encrypted_summoner_id,
        )
