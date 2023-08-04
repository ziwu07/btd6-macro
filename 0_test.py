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

wait(2)
place(x=2079, y=671,type='z')
upgrade('/ / / / . .')
place(x=1117, y=928,type='a')
upgrade(', , , , / /')