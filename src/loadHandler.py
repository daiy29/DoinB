from riotwatcher import LolWatcher, ApiError
import requests
from dotenv import load_dotenv
import logging
import os
import re

load_dotenv()
api_key = os.environ.get('API_KEY')
my_region = os.environ.get('REGION')
player_list = os.environ.get('PLAYERLIST')
certificate = os.environ.get('CERTIFICATE')
all_data = os.environ.get('ALLGAMEDATA')

lol_watcher = LolWatcher(api_key)

try:
    url = requests.get(player_list, verify=False)  #verify=certificate
except Exception as e:
    logging.exception("API call has failed")

try:
    url_all = requests.get(all_data, verify=False)
except Exception as e:
    logging.exception("API call has failed")

gamedata = url.json()
allgamedata = url_all.json()

def requestSummonerTeam(data):
    teams = []
    for summoner in data:
        teams.append(summoner["team"])
    return teams

def requestSummonerName(data):
    summoner_names = []
    for summoner in data:
        summoner_names.append(summoner["summonerName"])
    return summoner_names

def requestSummonerId(region): #hardcoded my shit for testing, need to change later. Maybe should move api request outside of method.
    try:
        data = lol_watcher.summoner.by_name(region, 'Legendai') #if using api, can change to use api error method
    except Exception as e:
        logging.exception("API call has failed")
    summoner_id = data["id"]
    return summoner_id

def requestSpellId(region, summonerid): #old verison
    try:
        data = lol_watcher.spectator.by_summoner(region, summonerid)
    except Exception as e:
        logging.exception("API call has failed")
    spell1_id = data["participants"][0]["spell1Id"]
    spell2_id = data["participants"][0]["spell2Id"]
    return ([spell1_id,spell2_id])

def requestSpellId2(data): # need to do a specific check for unleashed teleport later
    summoner_spells = []
    for summoner in data:
        summoner_spells.append([summoner["summonerSpells"]["summonerSpellOne"]["displayName"],summoner["summonerSpells"]["summonerSpellTwo"]["displayName"]])
    return summoner_spells

def requestRuneId(region, summonerid): # need something that parses perk ids to actual rune, but this is sufficient for now
    try:
        data = lol_watcher.spectator.by_summoner(region, summonerid)
    except Exception as e:
        logging.exception("API call has failed")
    rune_id = data["participants"][0]["perks"]
    return (rune_id)

def hasCosmic(rune_list):
    hasCosmic = False
    for rune_ids in rune_list:
        if rune_ids == 8347:
            hasCosmic = True
    return hasCosmic
        

def requestChampId(data):
    champ_ids = []
    for summoner in data:
        champ_ids.append(re.sub("[^a-zA-Z]+", "", summoner["championName"]))#strip whitespaces, apostrophe
    return champ_ids


def requestSummonerLevel():
    pass

def requestSummonerItems(data): #temp only check for ionians
    ionians = []
    for items in data:
        hasIonians = False
        for item in items["items"]:
            if item["displayName"] == "Ionian Boots of Lucidity":
                hasIonians = True
        ionians.append(hasIonians)
    return ionians
    # print(ionians)


def requestSummonerPosition(): #https://riot-api-libraries.readthedocs.io/en/latest/roleid.html
    pass

def requestGameTime(allgamedata):
    return allgamedata["gameData"]["gameTime"]

#print(requestSummonerItems(gamedata))
#add check for not in game maybe?, add class for runes, summoner spells??
