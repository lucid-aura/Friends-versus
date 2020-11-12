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