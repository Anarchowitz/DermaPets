import pyautogui as pyg
import pydirectinput as pyd
from tqdm import tqdm # useless
import random
import os
import keyboard
from time import sleep

os.makedirs("C:/DermaPets", exist_ok=True)
os.makedirs("C:/DermaPets/assets", exist_ok=True)
os.system('cls & title DermaPets')
active = False
values = ['groundpound', 'blackhole', 'chestspell', 'tornado', 'petsurge', 'tntshower']

def main():
    os.system('pause & cls')
    try:
        print("""
        1.AutoUltimate
        2.HugeDropNotification
        3.SimpleAFK
        4.[DEV] Position mouse/get resolution
        """)
        ans = input(" Selected method: ")
        if ans == "1":
            os.system('pause & cls')
            print('Press "INSERT" to activate')
            ault()
        elif ans == "2":
            os.system('pause & cls')
            print('Press "INSERT" to activate')
            hdrop()
        elif ans == "3":
            os.system('pause & cls')
            print('Press "INSERT" to activate')
            safk()
        elif ans == "4":
            os.system('pause & cls')
            sizpos()
        else:
            print("\n [ERROR] CHOOSE NUMBER! (1-3)")
            sleep(1)
            os.system('cls')
            main()
    except KeyboardInterrupt:
        os._exit(1)

#----------------------------------------
# 1.AutoUltimate
def ault():
    while True:
        try:
            sleep(2)
            find_and_click(r"C:/DermaPets/assets/ultimate.png")
        except pyg.ImageNotFoundException:  
            pass

def find_and_click(button_image):
    if active:
        button_location = None
        while button_location is None:
            button_location = pyg.locateOnScreen(button_image, grayscale=True, confidence=0.8)
        button_x, button_y = pyg.center(button_location)
        sleep(0.5)
        print('[DEBUG]', 'button coords', button_x, button_y)
        pyd.press('r')
def toggle_activation():
    global active
    active = not active
    if active:
        pyg.alert(text='Activated', title='DermaPets', button='OK')
        print('Activated')
    else:
        pyg.alert(text='Deactivated', title='DermaPets', button='OK')
        print('Deactivated')
# ---------------------------------------
# 2.HugeDropNotification
def hdrop():
    while True:
        try:
            sleep(0.05)
            find_and_click2(r"C:/DermaPets/assets/cloud.png")
        except pyg.ImageNotFoundException:  
            pass
def find_and_click2(button_image):
    if active:
        button_location = None
        while button_location is None:
            button_location = pyg.locateOnScreen(button_image, confidence=0.7)
        button_x, button_y = pyg.center(button_location)
        sleep(0.5)
        print('[DEBUG]', 'Finded', button_x, button_y)

# ---------------------------------------
# 3.SimpleAFK
def safk():
    while True:
        sleep(5)
        mafk()
def mafk():
    if active:
        sleep(5)
        pyd.press('space')
        sleep(1)
        pyd.press('space')
# ---------------------------------------
# 4.DEV
def sizpos():
    siz = pyg.size() # экран
    pos = pyg.position()
    print(f'Resolution: {siz} \nPosition mouse:{pos}')

keyboard.add_hotkey('insert', toggle_activation)
if __name__ == "__main__":
    for i in tqdm(range(1), desc='PATCHING'):
        sleep(random.randint(1, 2)) # idk why i added fake LOADING :)
    main()