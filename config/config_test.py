import sys 
from pprint import pprint 
sys.path.append('..')
from config import JsonConfig

if __name__ == "__main__":
    config = JsonConfig(configFile='Develop.json').config
    pprint(config)

