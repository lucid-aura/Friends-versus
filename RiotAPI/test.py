from LolWatcher import LolWatcher


# 라이엇 json
def test_get_version(API_KEY, REGION):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_versions = lolwatcher.datadragon.versions_for_region(REGION)
    print(resp_lol_versions.text)

def test_get_champion_per_version_locale(API_KEY, VERSION, FULL, LOCALE):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_champions = lolwatcher.datadragon.champions(VERSION, FULL, LOCALE)
    print(resp_lol_champions.text)

def test_get_items_per_version_locale(API_KEY, VERSION, LOCALE):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_items = lolwatcher.datadragon.items(VERSION, LOCALE)
    print(resp_lol_items.text)

def test_get_runes_per_version_locale(API_KEY, VERSION, LOCALE):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_runes = lolwatcher.datadragon.runes(VERSION, LOCALE)
    print(resp_lol_runes.text)

def test_get_runes_reforged_per_version_locale(API_KEY, VERSION, LOCALE):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_runes_reforged = lolwatcher.datadragon.runes_reforged(VERSION, LOCALE)
    print(resp_lol_runes_reforged.text)

def test_get_summoner_spells_per_version_locale(API_KEY, VERSION, LOCALE):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_summoner_spells = lolwatcher.datadragon.summoner_spells(VERSION, LOCALE)
    print(resp_lol_summoner_spells.text)


# 소환사 정보
def test_get_summoner_info_by_account(API_KEY, REGION, ENCRYPTED_ACCOUNT_ID):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_summoner_info_by_account = lolwatcher.summoner.by_account(REGION, ENCRYPTED_SUMMONER_ID)
    print(resp_lol_summoner_info_by_account.text)

def test_get_summoner_info_by_name(API_KEY, REGION, SUMMONER_NAME):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_summoner_info_by_name = lolwatcher.summoner.by_name(REGION, SUMMONER_NAME)
    print(resp_lol_summoner_info_by_name.text)

def test_get_summoner_info_by_puuid(API_KEY, REGION, ENCRYPTED_PUUID):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_summoner_info_by_puuid = lolwatcher.summoner.by_puuid(REGION, ENCRYPTED_PUUID)
    print(resp_lol_summoner_info_by_puuid.text)

def test_get_summoner_info_by_id(API_KEY, REGION, ENCRYPTED_SUMMONER_ID):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_summoner_info_by_id = lolwatcher.summoner.by_id(REGION, ENCRYPTED_SUMMONER_ID)
    print(resp_lol_summoner_info_by_id.text)


# 챔피언 로테이션
def test_get_champion_rotation_per_region(API_KEY, REGION):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_champion_rotations = lolwatcher.championrotation.rotations(REGION)
    print(resp_lol_champion_rotations.text)


# 유저에 따른 챔피언 정보
def test_get_champion_mastery_by_summoner(API_KEY, REGION, ENCRYPTED_SUMMONER_ID):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_champion_mastery_by_summoner = lolwatcher.championmastery.by_summoner(REGION, ENCRYPTED_SUMMONER_ID)
    print(resp_lol_champion_mastery_by_summoner.text)

def test_get_champion_mastery_by_summoner_by_champion(API_KEY, REGION, ENCRYPTED_SUMMONER_ID, CHAMPION_ID):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_champion_mastery_by_summoner_by_champion = lolwatcher.championmastery.by_summoner_by_champion(REGION, ENCRYPTED_SUMMONER_ID, CHAMPION_ID)
    print(resp_lol_champion_mastery_by_summoner_by_champion.text)

def test_get_champion_mastery_scores_by_summoner(API_KEY, REGION, ENCRYPTED_SUMMONER_ID):
    lolwatcher = LolWatcher(API_KEY)
    resp_lol_champion_mastery_scores_by_summoner = lolwatcher.championmastery.scores_by_summoner(REGION, ENCRYPTED_SUMMONER_ID)
    print(resp_lol_champion_mastery_scores_by_summoner.text)


# 테스트 파라미터
API_KEY="RGAPI-330711e3-2f76-48c1-b832-6a455f132270"
REGION = "kr"
VERSION = "10.23.1"
FULL=False
LOCALE = "ko_KR"
ENCRYPTED_SUMMONER_ID = "DSysYVtTtCikX_KPElUN1FgzRcDzBwBuYOnYZ-rImUlAgg" #휘랑
SUMMONER_NAME = "휘랑"
ENCRYPTED_ACCOUNT_ID = "ocszCxil4hSsLfkm2jds_6p97_UDmFGe_95Fu37j9y7K"
ENCRYPTED_PUUID = "e0wX5c8UW2WFWhC36nKTi1c3NcALQoztvD9qjqgZNNoG97KHNth-acac1-a-BIIhtFN1U3fNH7KZ_w"
CHAMPION_ID = 1


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
    test_get_champion_mastery_scores_by_summoner(API_KEY, REGION, ENCRYPTED_SUMMONER_ID)
