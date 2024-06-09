import pyautogui
import webbrowser
import time

# Open the browser with a specific URL
webbrowser.open('https://www.instagram.com')
time.sleep(10)  # Wait for the browser to load

# Simulate typing and mouse clicks
pyautogui.write('username')
pyautogui.press('tab')
pyautogui.write('password')
pyautogui.press('enter')