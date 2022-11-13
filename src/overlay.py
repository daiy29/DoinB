import pygame
from pygame.locals import *
import win32api
import win32con
import win32gui, win32com.client
import time 

pygame.init()   
screen = pygame.display.set_mode((800, 600),pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (139, 0, 0)

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


while not done:     
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        # print(i)
        if "pygame window" in i[1].lower():
            # print(i, 'is found')
                win32gui.ShowWindow(i[0],5)
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(i[0])
                break
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_TAB:
                pygame.display.set_mode((1,1),pygame.NOFRAME)
        if event.type == KEYUP:
            if event.key == K_TAB:
                pygame.display.set_mode((800, 600),pygame.NOFRAME)
        if event.type == pygame.QUIT:
            done = True

    screen.fill(fuchsia)  # Transparent background
    pygame.draw.rect(screen, dark_red, pygame.Rect(30, 30, 60, 60))
    pygame.display.update()

#https://www.reddit.com/r/pygame/comments/m061fs/optimisation_wrt_transparent_overlays/
#https://stackoverflow.com/questions/550001/fully-transparent-windows-in-pygame
#https://stackoverflow.com/questions/63395415/how-to-change-focus-to-pygame-window