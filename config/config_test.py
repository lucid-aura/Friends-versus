from config import JsonConfig

if __name__ == "__main__":
    config = JsonConfig(configFile="Develop.json").config

    print(config)
    print(config["DATABASE"])
    print(config["DATABASE"]["MONGODB"])