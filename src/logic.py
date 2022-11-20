from tkinter import *
from functools import partial
import pyperclip
from monitorHandler import monitor_areas
from loadHandler import *
from conversion import msToTime
from summoner import Summoner
from sumHasteHandler import *
from timerQueue import timerQueue
#from copyPasteHandler import appendToCopy

opps = []
oppsidx = []
timings = timerQueue([],[],[])

champs = requestChampId(gamedata)
summoner_names = requestSummonerName(gamedata)
summoner_ids = []
haste = [0,0,0,0,0,0,0,0,0,0]
has_cosmic = []
has_ionians = requestSummonerItems(gamedata)
spells = requestSpellId2(gamedata)
teams = requestSummonerTeam(gamedata) # this isnt really needed, remove this later

me = allgamedata["activePlayer"]["summonerName"]
myTeam = ""
    
for i in range(0,len(summoner_names)):
    summoner_ids.append(requestSummonerId(my_region))
    all_runes = requestRuneId(my_region, summoner_ids[i])['perkIds']
    has_cosmic.append(hasCosmic(all_runes))

for i in range(0,len(summoner_names)): 
    if summoner_names[i] == me:
        myTeam = teams[i]
for i in range(0,len(summoner_names)):
    if teams[i] != myTeam:
        opps.append(Summoner(champs[i],summoner_ids[i],haste[i],has_cosmic[i],has_ionians[i],spells[i],teams[i]))
        oppsidx.append(i)

def update(gamedata):
    #we can update ionians, haste. For now we only need to check ionians
    has_ionians = requestSummonerItems(gamedata)
    for i in range(0,len(opps)):
        if opps[i].get_name() == champs[oppsidx[i]]:
            opps[i].set_ionians(has_ionians[i])
            opps[i].set_haste(getTotalSummonerHaste(opps[i].get_ionians(),opps[i].get_cosmic()))


def newRequest():
    try:
        new_url = requests.get(player_list, verify=False)
    except Exception as e:
        logging.exception("API call has failed")
    gamedata = new_url.json()
    return gamedata
    

def newAllRequest():
    try:
        new_all_url = requests.get(all_data, verify=False)
    except Exception as e:
        logging.exception("API call has failed")
    allgamedata = new_all_url.json()
    return allgamedata


def appendToCopy(str1, str2):
    str1.append(str2)
    pyperclip.copy(' '.join(str1))
    
###############################################################################################

def spellOneCallBack(players):
    gamedata = newRequest()
    allgamedata = newAllRequest()
    update(gamedata)
    timings.timeCollector(requestGameTime(allgamedata))
    #print(opps[players].get_summonerspells()[0])
    cooldown = calculateNewHaste(opps[players].get_summonerspells()[0], opps[players].get_ionians(), opps[players].get_cosmic())
    print(opps[players].get_name() + " " + opps[players].get_summonerspells()[0] + " " + msToTime(requestGameTime(allgamedata) + cooldown))
    timings.appendChampions(opps[players].get_name())
    timings.appendSpell(opps[players].get_summonerspells()[0])
    timings.appendTime(requestGameTime(allgamedata) + cooldown)
    pyperclip.copy(timings.toStr())


    # appendToCopy(timings, opps[players].get_name() + " " + opps[players].get_summonerspells()[0] + " " + msToTime(requestGameTime(allgamedata) + cooldown))

def spellTwoCallBack(players):
    gamedata = newRequest()
    allgamedata = newAllRequest()
    update(gamedata)
    #print(opps[players].get_summonerspells()[0])
    cooldown = calculateNewHaste(opps[players].get_summonerspells()[1], opps[players].get_ionians(), opps[players].get_cosmic())
    print(opps[players].get_name() + " " + opps[players].get_summonerspells()[0] + " " + msToTime(requestGameTime(allgamedata) + cooldown))
    appendToCopy(timings, opps[players].get_name() + " " + opps[players].get_summonerspells()[0] + " " + msToTime(requestGameTime(allgamedata) + cooldown))

