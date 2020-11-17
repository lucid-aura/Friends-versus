from ..Endpoint import Endpoint


class LeagueEndpoint:
    def __init__(self,
        url: str,
        **kwargs):
        
        self.__root_url = "https://{platform}.api.riotgames.com"
        self._url = f"/lol{url}"

    def __call__(self, **kwargs):
        final_url = f"{self.__root_url}{self._url}"

        endpoint = Endpoint(final_url, **kwargs)
        return endpoint(**kwargs)
