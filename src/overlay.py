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
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)     #win32con.WS_EX_TRANSPARENT allows click thru
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

#i don't know what the fuck I did but it works for now, don't change this lol"


while not done:     


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_TAB:
                pygame.display.set_mode((1,1),pygame.NOFRAME)
        if event.type == KEYUP:
            if event.key == K_TAB:      
                pygame.display.set_mode((800, 600),pygame.NOFRAME)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 30 <= mouse[0] <= 60 and 30 <= mouse[1] <= 60:
                print("click")
        if event.type == pygame.QUIT:
            done = True

    screen.fill(fuchsia)  # Transparent background
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], -1, 800, 600, 0, 0, 1)
    pygame.draw.rect(screen, dark_red, pygame.Rect(30, 30, 60, 60))
    mouse = pygame.mouse.get_pos()
    pygame.display.update()

#https://www.reddit.com/r/pygame/comments/m061fs/optimisation_wrt_transparent_overlays/
#https://stackoverflow.com/questions/550001/fully-transparent-windows-in-pygame
#https://stackoverflow.com/questions/63395415/how-to-change-focus-to-pygame-window