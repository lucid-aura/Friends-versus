# SummonerAPIv4
from ..BaseAPI import BaseAPI
from ..NamedEndpoint import NamedEndpoint
from .LeagueEndpoint import LeagueEndpoint
# urls/SummonerAPIUrl

class SummonerEndpoint(LeagueEndpoint):
    def __init__(self,
        url: str,
        **kwargs):
        nurl = f"/summoner/v4/summoners{url}"
        super().__init__(nurl, **kwargs)

class SummonerAPIUrls:
    by_account = SummonerEndpoint("/by-account{encrypted_account_id}")
    by_name = SummonerEndpoint("/by-name/{summoner_name}")
    by_puuid = SummonerEndpoint("/by_puuid/{encrypted_puuid}")
    by_id = SummonerEndpoint("/{encrypted_summoner_id}")


class SummonerAPI(NamedEndpoint):
    """
    Summoner endpoint를 랩핑하는 클래스
    https://developer.riotgames.com/api-methods/#summoner-v4 
    """
    def __init__(self, base_api: BaseAPI):
        super().__init__(base_api, self.__class__.__name__)


    def by_account(self, 
        region: str,
        encrypted_account_id: str):
        """
        소환사를 account ID로 가져옴
        :param string region : region
        :param string encrypted_account_id : account ID
        :returns : SummonerDTD : 소환사
        """
        return self._request_endpoint(
            self.by_account.__name__,
            region,
            SummonerAPIUrls.by_account,
            encrypted_account_id=encrypted_account_id,
        )
    
    def by_name(self,
        region: str,
        summoner_name: str):
        """
        소환사를 summoner name로 가져옴
        :param string region: 
        :param string summoner_name : Summoner Name
        :returns : SummonerDTD : 소환사
        """
        return self._request_endpoint(
            self.by_name.__name__,
            region,
            SummonerAPIUrls.by_name,
            summoner_name=summoner_name,
        )
    
    def by_puuid(self,
        region: str,
        encrypted_puuid: str):
        """
        소환사를 PUUID로 가져옴
        :param string region: 
        :param string encrypted_puuid : PUUID
        :returns : SummonerDTD : 소환사
        """
        return self._request_endpoint(
            self.by_puuid.__name__,
            region,
            SummonerAPIUrls.by_puuid,
            encrypted_puuid=encrypted_puuid,
        )

    def by_id(self,
        region: str,
        encrypted_summoner_id: str):
        """
        소환사를 summoner ID로 가져옴
        :param string region:
        :param string encrypted_summoner_id: Summoner ID
        :returns : SummonerDTD : 소환사
        """
        return self._request_endpoint(
            self.by_id.__name__,
            region,
            SummonerAPIUrls.by_id,
            encrypted_summoner_id=encrypted_summoner_id,
        )
