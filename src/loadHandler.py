from riotwatcher import LolWatcher, ApiError
import requests
from dotenv import load_dotenv
import logging
import os

load_dotenv()
api_key = os.environ.get('API_KEY')
my_region = os.environ.get('REGION')
player_list = os.environ.get('PLAYERLIST')
certificate = os.environ.get('CERTIFICATE')

lol_watcher = LolWatcher(api_key)

try:
    url = requests.get(player_list, verify=certificate) 
except Exception as e:
    logging.exception("API call has failed")

gamedata = url.json()

def requestSummonerTeam(data):
    for summoner in data:
        team = summoner["team"]
    return team

def requestSummonerName(data):
    for summoner in data:
        summoner_name = summoner["summonerName"]
    return summoner_name

def requestSummonerId(region): #hardcoded my shit for testing, need to change later. Maybe should move api request outside of method.
    try:
        data = lol_watcher.summoner.by_name(region, 'Legendai') #if using api, can change to use api error method
    except Exception as e:
        logging.exception("API call has failed")
    summoner_id = data["id"]
    return summoner_id

def requestSpellId(region, summonerid):
    try:
        data = lol_watcher.spectator.by_summoner(region, summonerid)
    except Exception as e:
        logging.exception("API call has failed")
    spell1_id = data["participants"][0]["spell1Id"]
    spell2_id = data["participants"][0]["spell2Id"]
    return ([spell1_id,spell2_id])

def requestRuneId(region, summonerid): # need something that parses perk ids to actual rune, but this is sufficient for now
    try:
        data = lol_watcher.spectator.by_summoner(region, summonerid)
    except Exception as e:
        logging.exception("API call has failed")
    rune_id = data["participants"][0]["perks"]
    return (rune_id)

def requestChampId():
    pass

def requestSummonerLevel():
    pass

def requestSummonerItems():
    pass

def requestSummonerPosition(): #https://riot-api-libraries.readthedocs.io/en/latest/roleid.html
    pass

def requestGameTime():
    pass


#add check for not in game maybe?, add class for runes, summoner spells??
