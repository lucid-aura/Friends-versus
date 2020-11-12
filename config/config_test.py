import sys 

sys.path.append('..')
from config.config import JsonConfig

if __name__ == "__main__":
    config = JsonConfig(configFile='Develop.json').config
    print(config)
