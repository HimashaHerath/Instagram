import cv2
import numpy as np
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
username_value = os.getenv('USERNAME_VALUE', 'default_username')
password_value = os.getenv('PASSWORD_VALUE', 'default_password')

# Load images
ui_image = cv2.imread(r"Login\openCV\UI.png")
login_template = cv2.imread(r"Login\openCV\username.png")
password_template = cv2.imread(r"Login\openCV\password.png")
login_button_template = cv2.imread(r'Login\openCV\loginButton.png')

# Template matching
result_login = cv2.matchTemplate(ui_image, login_template, cv2.TM_CCOEFF_NORMED)
result_password = cv2.matchTemplate(ui_image, password_template, cv2.TM_CCOEFF_NORMED)
result_login_button = cv2.matchTemplate(ui_image, login_button_template, cv2.TM_CCOEFF_NORMED)

# Get coordinates of the best match
min_val, max_val, min_loc, max_loc_login = cv2.minMaxLoc(result_login)
min_val, max_val, min_loc, max_loc_password = cv2.minMaxLoc(result_password)
min_val, max_val, min_loc, max_loc_login_button = cv2.minMaxLoc(result_login_button)

# Get the dimensions of the templates
login_height, login_width = login_template.shape[:2]
password_height, password_width = password_template.shape[:2]
login_button_height, login_button_width = login_button_template.shape[:2]

# Calculate the center coordinates of the login and password fields and the login button
login_center = (max_loc_login[0] + login_width // 2, max_loc_login[1] + login_height // 2)
password_center = (max_loc_password[0] + password_width // 2, max_loc_password[1] + password_height // 2)
login_button_center = (max_loc_login_button[0] + login_button_width // 2, max_loc_login_button[1] + login_button_height // 2)

# Create JSON data
data = [
    {
        "id": "username",
        "x": login_center[0],
        "y": login_center[1],
        "button": "left",
        "clicks": 2,
        "interval": 1,
        "typingValue": username_value
    },
    {
        "id": "password",
        "x": password_center[0],
        "y": password_center[1],
        "button": "left",
        "clicks": 2,
        "interval": 1,
        "typingValue": password_value
    },
    {
        "id": "loginbutton",
        "x": login_button_center[0],
        "y": login_button_center[1],
        "button": "left",
        "clicks": 2,
        "interval": 1,
        "typingValue": ""
    }
]

# Write data to a JSON file
with open('coordinates_and_values.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file has been written with the coordinates and values.")
