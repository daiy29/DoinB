from tkinter import *
from functools import partial
import pyperclip
from monitorHandler import monitor_areas
from loadHandler import *
from conversion import msToTime
from summoner import Summoner

monitors = monitor_areas()
m1_res = str(monitors[0][2]) + 'x' + str(monitors[0][3])
m2_res = str(monitors[1][0]) + '+0'

window = Tk()

window.title("Summoner Spell Tracker")
window.geometry(m1_res)
window.geometry(m2_res)

champButtons=[]
timings=[]

champs = requestChampId(gamedata)
teams = requestSummonerTeam(gamedata) # this isnt really needed, remove this later
spells = requestSpellId2(gamedata)


opps = []
opps_spells = []

for x in range(0,len(champs)):
    if teams[x] == 'CHAOS':
        opps.append(champs[x])
        opps_spells.append(spells[x])

# opp_champion_1 = Champion(champs[5],)


champ_portraits = []
spell_icons = []
for champs in opps:
    champ_portraits.append(PhotoImage(file = "./assets/champion_img/" + champs + ".png"))
for spells in opps_spells:
    spell_icons.append(PhotoImage(file = "./assets/summoners_img/" + spells[0] + ".png"))
    spell_icons.append(PhotoImage(file = "./assets/summoners_img/" + spells[1] + ".png"))

def appendToCopy(str1, str2):
    str1.append(str2)
    pyperclip.copy(' '.join(str1))
    

def champCallBack(players):
    if players == 0:
        print("first player: copied") 
        appendToCopy(timings, "first player: copied")
    else:
        print("other player: copied")
        appendToCopy(timings, "other player: copied")

    # print(players)

def spellCallBack(ctr):
    if ctr == 0:
        print(str(opps[0]) + ":" + str(opps_spells[0]))

ctr = 0 #buttons are cringe and i guess this is how ill implement it for now

for players in range(0,5):
    genButton = Button(window,text="test"+str(players),image=champ_portraits[players], command=partial(champCallBack, players))
    champButtons.append(genButton)
    champButtons[players].grid(row=players,column=0)
    for spells in range(1,3):
        spell=Button(window,text="test"+str(spells),image=spell_icons[ctr],command=partial(spellCallBack, players))
        ctr+=1
        spell.grid(row=players,column=spells)

def hasteLoop():
    pass

window.mainloop()