from LolWatcher import LolWatcher
from requests import Response
import json 
if __name__ == "__main__":
    lol_watcher = LolWatcher("RGAPI-330711e3-2f76-48c1-b832-6a455f132270")
    my_region = 'kr'

    my_ranked_stats_response = lol_watcher._summoner.by_name(my_region, "휘랑")

    print(f"Status Code - {my_ranked_stats_response.status_code}")
    print(f"Response Json - {json.loads(my_ranked_stats_response.text)}")

"""
import sys 
import requests 
import pprint 
sys.path.append('..')
from config.config import JsonConfig

APIURL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
APIKEY = "RGAPI-330711e3-2f76-48c1-b832-6a455f132270"
SUMMONERNAME = "휘랑"
if __name__ == "__main__":
    config = JsonConfig(configFile='Develop.json').config
    pprint.pprint(config)

    sowhansa = APIURL + SUMMONERNAME + "?api_key=" + APIKEY

    resp = requests.get(sowhansa)
    pprint.pprint(resp.json())
"""