import os
import pyautogui
import time
import json

chrome_path = r'"C:/Program Files/Google/Chrome/Application/chrome.exe"'
url = 'https://instagram.com/accounts/login/?hl=en'

os.system(f'{chrome_path} --incognito {url}')

time.sleep(10)  

with open('coordinates_and_values.json', 'r') as file:
    actions = json.load(file)

for action in actions:
    pyautogui.moveTo(action['x'], action['y'], duration=1)
    
    pyautogui.click(clicks=action['clicks'], interval=action['interval'])

    if action['typingValue']:
        pyautogui.typewrite(action['typingValue'], interval=0.25)

    time.sleep(1)

print("Action sequence completed.")
