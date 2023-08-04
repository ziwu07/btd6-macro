import pyautogui
import time
import keyboard

def key(key:str):
    keyboard.press_and_release(key)
    wait()

def wait(t:float=0.03):
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
    place(x=1758, y=303,type='u')
    place(x=1164, y=274,type='i')
    upgrade('/ / / / , ,')
    click(x=501, y=404)
    click(x=1253, y=169)
    place(x=1140, y=380 ,type='i')
    upgrade(', , , / /')
    click(x=507, y=299)
    click(x=1538, y=253)
    click(x=649, y=1052)
    click(x=1164, y=274)
    click(x=1164, y=274)
    click(x=643, y=656)
    click(x=1140, y=380)


wait(4)
while True:
    click(x=1119, y=1246)
    click(x=776, y=1307)
    click(x=1278, y=360)
    click(x=860, y=578)
    click(x=1709, y=609)
    wait(4)
    click(x=1281, y=1010)
    wait(1)
    setup()
    start()
    time.sleep(390)
    wait(1)
    pyautogui.moveTo(x=1282, y=1211)
    wait_long()
    pyautogui.click(x=1282, y=1211)
    wait_long()
    click(x=956, y=1131)
    wait(2)
    