from tkinter import *
from functools import partial
import pyperclip
from monitorHandler import monitor_areas
from loadHandler import *
from conversion import msToTime
from summoner import Summoner
from sumHasteHandler import *
from logic import *
import subprocess

monitors = monitor_areas()
m1_res = str(monitors[0][2]) + 'x' + str(monitors[0][3])
m2_res = str(monitors[1][0]) + '+0'

window = Tk()

window.title("Summoner Spell Tracker")
window.geometry(m1_res)
window.geometry(m2_res)

"""
opps = []
oppsidx = []


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


"""
champ_portraits = []
spell_icons = []
for champs in opps:
    champ_portraits.append(PhotoImage(file = "./assets/champion_img/" + champs.get_name() + ".png"))
    spell_icons.append(PhotoImage(file = "./assets/summoners_img/" + champs.get_summonerspells()[0] + ".png"))
    spell_icons.append(PhotoImage(file = "./assets/summoners_img/" + champs.get_summonerspells()[1] + ".png"))
    

def champCallBack(players):
    """
     if players == 0:
        print("first player: copied") 
        appendToCopy(timings, "first player: copied")
    else:
        print("other player: copied")
        appendToCopy(timings, "other player: copied")
    """
    pass
    # print(players)


for players in range(0,5):
    s1 = 2*players
    s2 = 2*players+1
    champButton = Button(window,text="test"+str(players),image=champ_portraits[players], command=partial(champCallBack, players))
    champButton.grid(row=players,column=0)
    spellButton1 = Button(window,text="test"+str(spells),image=spell_icons[s1],command=partial(spellOneCallBack, players))
    spellButton2 = Button(window,text="test"+str(spells),image=spell_icons[s2],command=partial(spellTwoCallBack, players))
    spellButton1.grid(row=players,column=1)
    spellButton2.grid(row=players,column=2)

process = subprocess.Popen(['python', 'src/copyPasteHandler.py'])

window.mainloop()

        