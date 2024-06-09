import os
import pyautogui
import time
import json

# Path to Chrome executable
chrome_path = r'"C:/Program Files/Google/Chrome/Application/chrome.exe"'
url = 'https://instagram.com/accounts/login/?hl=en'

# Open Chrome in incognito mode and navigate to Instagram login page
os.system(f'{chrome_path} --incognito {url}')

# Allow some time for the browser to open and the page to load
time.sleep(10)  # Adjust this based on your computer's speed and internet connection

# Load coordinates and values from JSON
with open('coordinates_and_values.json', 'r') as file:
    actions = json.load(file)

# Perform the actions from the JSON file
for action in actions:
    # Move the cursor to the specific coordinates
    pyautogui.moveTo(action['x'], action['y'], duration=1)
    
    # Click the field based on the specified number of clicks and interval
    pyautogui.click(clicks=action['clicks'], interval=action['interval'])

    # Type the value if there is something to type
    if action['typingValue']:
        pyautogui.typewrite(action['typingValue'], interval=0.25)

    # Add a pause to simulate more human-like interaction
    time.sleep(1)

print("Action sequence completed.")
