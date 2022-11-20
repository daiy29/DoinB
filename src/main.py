from tkinter import *
from functools import partial
import pyperclip
import subprocess
from monitorHandler import monitor_areas
from loadHandler import *
from sumHasteHandler import *
from timerQueue import timerQueue
from summoner import Summoner

def drawGui():
    champ_portraits = []
    spell_icons = []
    monitors = monitor_areas()

    m1_res = str(monitors[0][2]) + 'x' + str(monitors[0][3])
    m2_res = str(monitors[1][0]) + '+0'

    window = Tk()
    window.title("Summoner Spell Tracker")
    window.geometry(m1_res)
    window.geometry(m2_res)

    for champs in opps:
        champ_portraits.append(PhotoImage(file = "./assets/champion_img/" + champs.get_name() + ".png"))
        spell_icons.append(PhotoImage(file = "./assets/summoners_img/" + champs.get_summonerspells()[0] + ".png"))
        spell_icons.append(PhotoImage(file = "./assets/summoners_img/" + champs.get_summonerspells()[1] + ".png"))
        
    for players in range(5):
        s1 = 2*players
        s2 = 2*players+1
        champButton = Button(window,text="test"+str(players),image=champ_portraits[players])
        champButton.grid(row=players,column=0)
        spellButton1 = Button(window,text="test"+str(spells),image=spell_icons[s1],command=partial(spellOneCallBack, players))
        spellButton2 = Button(window,text="test"+str(spells),image=spell_icons[s2],command=partial(spellTwoCallBack, players))
        spellButton1.grid(row=players,column=1)
        spellButton2.grid(row=players,column=2)

    subprocess.Popen(['python', 'src/copyPasteHandler.py'])
    window.mainloop()

def update(gamedata):
    #we can update ionians, haste. For now we only need to check ionians
    has_ionians = requestSummonerItems(gamedata)
    for i in range(len(opps)):
        if opps[i].get_name() == champs[oppsidx[i]]:
            opps[i].set_ionians(has_ionians[i])
            opps[i].set_haste(getTotalSummonerHaste(opps[i].get_ionians(),opps[i].get_cosmic()))

def newRequest():
    try:
        new_url = requests.get(player_list, verify=False)
    except Exception as e:
        logging.exception("API call has failed")
    gamedata = new_url.json()
    try:
        new_all_url = requests.get(all_data, verify=False)
    except Exception as e:
        logging.exception("API call has failed")
    allgamedata = new_all_url.json()

    return gamedata, allgamedata

timings = timerQueue([],[],[])

def spellOneCallBack(players):
    gamedata, allgamedata = newRequest()
    update(gamedata)
    timings.timeCollector(requestGameTime(allgamedata))
    cooldown = calculateNewHaste(opps[players].get_summonerspells()[0], opps[players].get_ionians(), opps[players].get_cosmic())
    # print(opps[players].get_name() + " " + opps[players].get_summonerspells()[0] + " " + msToTime(requestGameTime(allgamedata) + cooldown))
    timings.appendChampions(opps[players].get_name())
    timings.appendSpell(opps[players].get_summonerspells()[0])
    timings.appendTime(requestGameTime(allgamedata) + cooldown)
    pyperclip.copy(timings.toStr())


def spellTwoCallBack(players):
    gamedata, allgamedata = newRequest()
    update(gamedata)
    timings.timeCollector(requestGameTime(allgamedata))
    cooldown = calculateNewHaste(opps[players].get_summonerspells()[1], opps[players].get_ionians(), opps[players].get_cosmic())
    # print(opps[players].get_name() + " " + opps[players].get_summonerspells()[1] + " " + msToTime(requestGameTime(allgamedata) + cooldown))
    timings.appendChampions(opps[players].get_name())
    timings.appendSpell(opps[players].get_summonerspells()[1])
    timings.appendTime(requestGameTime(allgamedata) + cooldown)
    pyperclip.copy(timings.toStr())

if __name__ == "__main__":
    champs = requestChampId(gamedata)
    summoner_names = requestSummonerName(gamedata)
    has_ionians = requestSummonerItems(gamedata)
    spells = requestSpellId2(gamedata)
    teams = requestSummonerTeam(gamedata) # this isnt really needed, remove this later
    summoner_ids, has_cosmic = [], []
    haste = [0]*10

    for i in range(len(summoner_names)):
        summoner_ids.append(requestSummonerId(my_region, "Legendai"))
        all_runes = requestRuneId(my_region, summoner_ids[i])['perkIds']
        has_cosmic.append(hasCosmic(all_runes))

    me = allgamedata["activePlayer"]["summonerName"]
    myTeam = ""

    for i in range(len(summoner_names)): 
        if summoner_names[i] == me:
            myTeam = teams[i]

    opps = []
    oppsidx = []

    for i in range(len(summoner_names)):
        if teams[i] != myTeam:
            opps.append(Summoner(champs[i],summoner_ids[i],haste[i],has_cosmic[i],has_ionians[i],spells[i],teams[i]))
            oppsidx.append(i)
    
    drawGui()
