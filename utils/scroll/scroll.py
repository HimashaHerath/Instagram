import webbrowser
import pyautogui
import time

def open_url_and_scroll(url, x, y):
    # Open the URL
    webbrowser.open(url)
    
    # Wait for the page to load
    time.sleep(5)  # Adjust the timing based on your internet speed and page load time
    
    # Move the cursor to the specified coordinates
    pyautogui.moveTo(x, y)
    
    # Scroll to the end of the page
    # - Number of scrolls needed may vary based on page length; adjust as necessary
    while True:
        scroll_amount = pyautogui.scroll(-1000)  # Scrolls up 1000 "clicks"
        if not scroll_amount:
            break

    print("Reached the end of the page.")

# Example usage
open_url_and_scroll('https://www.instagram.com/p/C7OjExPIGJZ/', 1247, 159)  # Replace 500, 500 with your desired coordinates
