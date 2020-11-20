from riotwatcher import LolWatcher, ApiError
import pprint 
lol_watcher = LolWatcher("RGAPI-330711e3-2f76-48c1-b832-6a455f132270")

my_region = 'kr'

me = lol_watcher.summoner.by_name(my_region, '휘랑')
pprint.pprint(me)

# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
pprint.pprint(my_ranked_stats)

