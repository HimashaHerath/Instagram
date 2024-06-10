import webbrowser
import pyautogui
import time
import os
from PIL import ImageChops

def open_url_and_scroll(url, x, y):
    webbrowser.open(url)
    time.sleep(5)

    pyautogui.moveTo(x, y)
    
    screenshots_dir = 'utils\scroll\web_screenshots'
    os.makedirs(screenshots_dir, exist_ok=True)

    screenshot_index = 0
    last_screenshot = None
    attempts_without_scroll = 0

    while True:
        screenshot = pyautogui.screenshot()
        screenshot_path = os.path.join(screenshots_dir, f'screenshot_{screenshot_index}.png')
        screenshot.save(screenshot_path)
        print(f"Screenshot saved as {screenshot_path}")
        screenshot_index += 1

        if last_screenshot:
            difference = ImageChops.difference(screenshot, last_screenshot)
            if not difference.getbbox():
                attempts_without_scroll += 1
                if attempts_without_scroll > 3:
                    print("Reached the end of the scrollable area.")
                    break
            else:
                attempts_without_scroll = 0

        last_screenshot = screenshot
        pyautogui.scroll(-1000)
        time.sleep(2)


open_url_and_scroll('https://www.instagram.com/p/C71p6jsqXAZ/', 1234, 558)
