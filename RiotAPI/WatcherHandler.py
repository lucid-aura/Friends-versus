from LolWatcher import LolWatcher

class WatcherHandler:
    def __init__(self):
        # 테스트 파라미터
        self.API_KEY="RGAPI-330711e3-2f76-48c1-b832-6a455f132270"
        self.REGION = "kr"
        self.VERSION = "10.24.1"
        self.FULL=False
        self.LOCALE = "ko_KR"
        self.ENCRYPTED_SUMMONER_ID = "DSysYVtTtCikX_KPElUN1FgzRcDzBwBuYOnYZ-rImUlAgg" #휘랑
        self.SUMMONER_NAME = "휘랑"
        self.ENCRYPTED_ACCOUNT_ID = "ocszCxil4hSsLfkm2jds_6p97_UDmFGe_95Fu37j9y7K"
        self.ENCRYPTED_PUUID = "e0wX5c8UW2WFWhC36nKTi1c3NcALQoztvD9qjqgZNNoG97KHNth-acac1-a-BIIhtFN1U3fNH7KZ_w"
        self.CHAMPION_ID = 1
        self.lolwatcher = LolWatcher(self.API_KEY)
    # 라이엇 json
    def test_get_version(self):
        resp_lol_versions = self.lolwatcher.datadragon.versions_for_region(self.REGION)
        print(resp_lol_versions.json())
        return resp_lol_versions.json()

    def test_get_champion_per_version_locale(self):
        resp_lol_champions = self.lolwatcher.datadragon.champions(self.VERSION, self.FULL, self.LOCALE)
        print(resp_lol_champions.json())
        return resp_lol_champions.json()

    def test_get_items_per_version_locale(self):
        resp_lol_items = self.lolwatcher.datadragon.items(self.VERSION, self.LOCALE)
        print(resp_lol_items.json())
        return resp_lol_items.json()

    def test_get_runes_per_version_locale(self):
        resp_lol_runes = self.lolwatcher.datadragon.runes(self.VERSION, self.LOCALE)
        print(resp_lol_runes.json())
        return resp_lol_runes.json()

    def test_get_runes_reforged_per_version_locale(self):
        resp_lol_runes_reforged = self.lolwatcher.datadragon.runes_reforged(self.VERSION, self.LOCALE)
        print(resp_lol_runes_reforged.json())
        return resp_lol_runes_reforged.json()

    def test_get_summoner_spells_per_version_locale(self):
        resp_lol_summoner_spells = self.lolwatcher.datadragon.summoner_spells(self.VERSION, self.LOCALE)
        print(resp_lol_summoner_spells.json())
        return resp_lol_summoner_spells.json()


    # 소환사 정보
    def test_get_summoner_info_by_account(self):
        resp_lol_summoner_info_by_account = self.lolwatcher.summoner.by_account(self.REGION, self.ENCRYPTED_SUMMONER_ID)
        print(resp_lol_summoner_info_by_account.json())
        return resp_lol_summoner_info_by_account.json()

    def test_get_summoner_info_by_name(self):
        resp_lol_summoner_info_by_name = self.lolwatcher.summoner.by_name(self.REGION, self.SUMMONER_NAME)
        print(resp_lol_summoner_info_by_name.json())
        return resp_lol_summoner_info_by_name.json()

    def test_get_summoner_info_by_puuid(self):
        resp_lol_summoner_info_by_puuid = self.lolwatcher.summoner.by_puuid(self.REGION, self.ENCRYPTED_PUUID)
        print(resp_lol_summoner_info_by_puuid.json())
        return resp_lol_summoner_info_by_puuid.json()

    def test_get_summoner_info_by_id(self):
        resp_lol_summoner_info_by_id = self.lolwatcher.summoner.by_id(self.REGION, self.ENCRYPTED_SUMMONER_ID)
        print(resp_lol_summoner_info_by_id.json())
        return resp_lol_summoner_info_by_id.json()


    # 챔피언 로테이션
    def test_get_champion_rotation_per_region(self):
        resp_lol_champion_rotations = self.lolwatcher.championrotation.rotations(self.REGION)
        print(resp_lol_champion_rotations.json())
        return resp_lol_champion_rotations.json()


    # 유저에 따른 챔피언 정보
    def test_get_champion_mastery_by_summoner(self):
        resp_lol_champion_mastery_by_summoner = self.lolwatcher.championmastery.by_summoner(self.REGION, self.ENCRYPTED_SUMMONER_ID)
        print(resp_lol_champion_mastery_by_summoner.json())
        return resp_lol_champion_mastery_by_summoner.json()

    def test_get_champion_mastery_by_summoner_by_champion(self):
        resp_lol_champion_mastery_by_summoner_by_champion = self.lolwatcher.championmastery.by_summoner_by_champion(self.REGION, self.ENCRYPTED_SUMMONER_ID, CHAMPION_ID)
        print(resp_lol_champion_mastery_by_summoner_by_champion.json())
        return resp_lol_champion_mastery_by_summoner_by_champion.json()

    def test_get_champion_mastery_scores_by_summoner(self):
        resp_lol_champion_mastery_scores_by_summoner = self.lolwatcher.championmastery.scores_by_summoner(self.REGION, self.ENCRYPTED_SUMMONER_ID)
        print(resp_lol_champion_mastery_scores_by_summoner.json())
        return resp_lol_champion_mastery_scores_by_summoner.json()





if __name__ == "__main__":    
    """
    test_get_version(API_KEY, REGION)
    test_get_champion_per_version_locale(API_KEY, VERSION, FULL, LOCALE)
    test_get_items_per_version_locale(API_KEY, VERSION, LOCALE)
    test_get_runes_per_version_locale(API_KEY, "7.23.1", LOCALE)
    test_get_runes_reforged_per_version_locale(API_KEY, VERSION, LOCALE)
    test_get_summoner_spells_per_version_locale(API_KEY, "10.23.1", LOCALE)
    """
    """
    test_get_champion_rotation_per_region(API_KEY, REGION)
    """
    """     
    test_get_summoner_info_by_account(API_KEY, REGION, ENCRYPTED_ACCOUNT_ID)
    test_get_summoner_info_by_name(API_KEY, REGION, SUMMONER_NAME)
    test_get_summoner_info_by_puuid(API_KEY, REGION, ENCRYPTED_PUUID)
    test_get_summoner_info_by_id(API_KEY, REGION, ENCRYPTED_SUMMONER_ID)
    """    
    
    #test_get_champion_mastery_by_summoner_id(API_KEY, REGION, ENCRYPTED_SUMMONER_ID)
    #test_get_champion_mastery_by_summoner_by_champion(API_KEY, REGION, ENCRYPTED_SUMMONER_ID, CHAMPION_ID)
    #test_get_champion_mastery_scores_by_summoner(API_KEY, REGION, ENCRYPTED_SUMMONER_ID)

    