from riotwatcher import LolWatcher, ApiError
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get('API_KEY')
my_region = os.environ.get('REGION')
player_list = os.environ.get('PLAYERLIST')
certificate = os.environ.get('CERTIFICATE')

lol_watcher = LolWatcher(api_key)

url = requests.get(player_list, verify=certificate) 
gamedata = url.json()

def requestSummonerTeam(data):
    for summoner in data:
        team = summoner["team"]
    return team

def requestSummonerName(data):
    for summoner in data:
        summoner_name = summoner["summonerName"]
    return summoner_name

def requestSummonerId(region):
    data = lol_watcher.summoner.by_name(region, 'Legendai')
    summoner_id = data["id"]
    return summoner_id

def requestSpellId(region, summonerid):
    data = lol_watcher.spectator.by_summoner(region, summonerid)
    spell1_id = data["participants"][0]["spell1Id"]
    spell2_id = data["participants"][0]["spell2Id"]
    return ([spell1_id,spell2_id])

def requestRuneId(region, summonerid):
    data = lol_watcher.spectator.by_summoner(region, summonerid)
    rune_id = data["participants"][0]["perks"]
    return (rune_id)

# need something that parses perk ids to actual rune, but this is sufficient for now

print(requestRuneId("na1","4lNm9p8Wucf3xDc4p5_cgaKhoJGrhL97KwGddhMJIs2vCuec"))

# def requestRuneID(summonerid)

#add check for not in game maybe?, add class for runes, summoner spells??

"""
# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

# First we get the latest version of the game from data dragon
versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']

# Lets get some champions
current_champ_list = lol_watcher.data_dragon.champions(champions_version)
print(current_champ_list)

# For Riot's API, the 404 status code indicates that the requested data wasn't found and
# should be expected to occur in normal operation, as in the case of a an
# invalid summoner name, match ID, etc.
#
# The 429 status code indicates that the user has sent too many requests
# in a given amount of time ("rate limiting").

try:
    response = lol_watcher.summoner.by_name(my_region, 'this_is_probably_not_anyones_summoner_name')
except ApiError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(err.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        raise

"""
