from tkinter import *
from functools import partial
import pyperclip

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('1920x1000')
window.geometry('-1920+0')

champButtons=[]
timings=[]

aatrox_img = PhotoImage(file = "./assets/champion_img/Aatrox.png")
flash_img = PhotoImage(file = "./assets/summoners_img/flash.png")

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

for players in range(0,5):
    genButton = Button(window,text="test"+str(players),image=aatrox_img, command=partial(champCallBack, players))
    champButtons.append(genButton)
    champButtons[players].grid(row=players,column=0)

    for spells in range(1,3):
        spell=Button(window,text="test"+str(spells),image=flash_img)
        spell.grid(row=players,column=spells)
window.mainloop()