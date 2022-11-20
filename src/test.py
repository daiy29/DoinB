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
summoner_names = requestSummonerName(gamedata)
summoner_ids = [0,0,0,0,0,0,0,0,0,0]
haste = [0,0,0,0,0,0,0,0,0,0]
has_cosmic = [0,0,0,0,0,0,0,0,0,0]
has_ionians = [0,0,0,0,0,0,0,0,0,0]
spells = requestSpellId2(gamedata)
teams = requestSummonerTeam(gamedata) # this isnt really needed, remove this later


print(summoner_names)
