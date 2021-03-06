import re 

from ..BaseAPI import BaseAPI
from ..NamedEndpoint import NamedEndpoint
from ..Endpoint import Endpoint

# http://ddragon.leagueoflegends.com/cdn/10.25.1/img/champion/Aatrox.png
# http://ddragon.leagueoflegends.com/cdn/10.25.1/img/passive/Zoe_P.png
# http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_0.jpg
# https://ddragon.leagueoflegends.com/api/versions.json

class DataDragonEndpoint(Endpoint):
    def __init__(self, url, **kwargs):
        nurl = f"https://ddragon.leagueoflegends.com{url}"
        super().__init__(nurl, **kwargs)

class DataDragonVersionLocaleEndpoint(DataDragonEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/cdn/{{version}}/data/{{locale}}{url}"
        super().__init__(nurl, **kwargs)

class DataDragonImgEndpoint(DataDragonEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/cdn/{{version}}/img/{{target}}{url}"
        super().__init__(nurl, **kwargs)

class DataDragonUrls:
    versions = DataDragonEndpoint("/realms/{region}.json")
    img_champion_loading = DataDragonEndpoint("/cdn/img/champion/loading/{skin_id}.jpg")
    img_champion_splash = DataDragonImgEndpoint("champion/splash/")
    img_champion_tiles = DataDragonImgEndpoint("champion/tiles/")
    championsFull = DataDragonVersionLocaleEndpoint("/championFull.json")
    champions = DataDragonVersionLocaleEndpoint("/champion.json")
    champion = DataDragonVersionLocaleEndpoint("/champion/")
    items = DataDragonVersionLocaleEndpoint("/item.json")
    runes = DataDragonVersionLocaleEndpoint("/rune.json")
    runes_reforged = DataDragonVersionLocaleEndpoint("/runesReforged.json")
    summoner_spells = DataDragonVersionLocaleEndpoint("/summoner.json")



class DataDragonAPI:
    def __init__(self, base_api: BaseAPI):
        self._base_api = base_api

    def _request(self, endpoint: Endpoint, version: str=None, locale: str=None):
        url, query = endpoint(version=version, locale=locale if locale else "ko_KR")
        print(url, " ^^ ")
        return self._base_api.raw_request_static(url, query)

    def loading_img(self, skin_id: str):
        #skin_id = re.sub(r"\s", "", skin_id)
        url, query = DataDragonUrls.img_champion_loading(skin_id=skin_id)
        print(url, " TT ")
        return self._base_api.raw_request_static(url, query)

    def versions_for_region(self, region: str):
        region = re.sub(r"\d", "", region)
        url, query = DataDragonUrls.versions(region=region)
        return self._base_api.raw_request_static(url, query)

    def champions(self, version: str, full: bool = False, locale: str =None):
        return self._request(
            DataDragonUrls.championsFull if full else DataDragonUrls.champions,
            version,
            locale,
        )

    def champion(self, version: str, locale: str =None, champion_id =""):
        path = "/champion/" + champion_id + ".json"
        return self._request(
            DataDragonVersionLocaleEndpoint(path),
            version,
            locale,
        )
        # return self._request(
        #     DataDragonUrls.champions,
        #     version,
        #     locale,
        # )

    def items(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.items, version, locale)

    def runes(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.runes, version, locale)

    def runes_reforged(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.runes_reforged, version, locale)
    
    def summoner_spells(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.summoner_spells, version, locale)