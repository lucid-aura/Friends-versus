import json

class JsonParser:
    def __init__(self, loaded_data):
        self.data = loaded_data
        #print(self.data)

    def parsing_data(self, loaded_data):
        print(loaded_data.values())

    def client_version(self):
        return self.data[0]

    def parsing_champion_data(self):
        # key가 "data"인 딕셔너리 가져오기
        champion_stat = []
        for key in self.data.keys():
            dic = dict()
            dic['id'] = key
            dic.update(self.data[key]['stats'])
            champion_stat.append(dic)
        return champion_stat
