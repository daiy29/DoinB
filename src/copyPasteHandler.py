import keyboard
import pyautogui
import pydirectinput
import pyperclip

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = 0

pressed = False

while True:
    if keyboard.is_pressed('v') and keyboard.is_pressed('ctrl'):
        if not pressed:
            pressed = True
            pydirectinput.press('enter') 
            pyautogui.write(pyperclip.paste())
    else:
        pressed = False

        
# https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game

# this is a wip, riots chat client uses it's own clipboard


 
