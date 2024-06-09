import subprocess

def open_chrome(url):
    # Path to Chrome executable
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    # Opening Chrome and navigating to the specified URL
    subprocess.Popen([chrome_path, url])

# Specify the URL
url = 'https://www.instagram.com'
open_chrome(url)
