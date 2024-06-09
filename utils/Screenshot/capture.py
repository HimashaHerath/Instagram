import webbrowser
import pyautogui
import time
import pygetwindow as gw

def take_screenshot(url, save_path='Template.png'):
    webbrowser.open(url)
    
    time.sleep(2)
    
    title = gw.getActiveWindowTitle()
    window = gw.getWindowsWithTitle(title)[0]
    
    if window is not None:
        window.maximize()
        time.sleep(5)
    else:
        print("Failed to find the browser window.")
        return
    
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)
    
    print(f"Screenshot saved as {save_path}")

# Example usage
take_screenshot('https://www.instagram.com/p/C7OjExPIGJZ/', 'Template.png')
