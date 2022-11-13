import win32gui
import time

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


results = []
top_windows = []
win32gui.EnumWindows(windowEnumerationHandler, top_windows)
for i in top_windows:
        print(i)
        if "pygame window" in i[1].lower():
            print(i, 'is found')
            while True:
                win32gui.ShowWindow(i[0],5)
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(i[0])
                time.sleep(1)