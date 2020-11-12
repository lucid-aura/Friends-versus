def client_version(self):
    json_parser = self.config["version"]
    return json_parser

def parsing_champion_data(self):
    # key가 "data"인 딕셔너리 가져오기
    json_parser = self.config["data"]
    champion_stat = []
    for key in json_parser.values():
        dic = dict()
        dic['id'] = key['id']
        dic.update(key['stats'])
        champion_stat.append(dic)
    return champion_stat