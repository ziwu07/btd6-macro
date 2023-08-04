import pyautogui
import time
import keyboard

def key(key:str):
    keyboard.press_and_release(key)
    wait()

def wait(t:float=0.2):
    time.sleep(t)

def wait_long(t:float=0.5):
    time.sleep(t)

def upgrade(upgrades:str):
    keys = upgrades.split()
    for num in keys:
        key(num)

def place(x:int,y:int,type:str):
    wait()
    key(type)
    pyautogui.moveTo(x=x,y=y)
    wait()
    pyautogui.click(x=x,y=y)
    wait()
    pyautogui.click(x=x,y=y)
    wait()

def click(x:int,y:int):
    wait_long()
    pyautogui.moveTo(x=x,y=y)
    wait_long()
    pyautogui.click(x=x,y=y)
    wait_long()

def start():
    wait()
    key('space')
    key('space')
    wait()

def setup():
    place(x=2079, y=671,type='z')
    upgrade('/ / / / . .')
    place(x=1117, y=930,type='a')
    upgrade(', , , , / /')


wait(4)
while True:
    click(x=1119, y=1246)
    click(x=1781, y=1303)
    click(x=1276, y=776)
    click(x=860, y=578)
    click(x=1709, y=609)
    wait(4)
    click(x=1281, y=1010)
    wait(1)
    setup()
    start()
    pyautogui.moveTo(x=1654, y=736)
    for i in range(360):
        pyautogui.click()
        time.sleep(1)
    wait(1)
    pyautogui.moveTo(x=1282, y=1211)
    wait_long()
    pyautogui.click(x=1282, y=1211)
    wait_long()
    click(x=956, y=1131)
    wait(2)