import cv2
import numpy as np

def match_template(image_path, template_path):
    img = cv2.imread(image_path, 0)
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    if not loc[0].size:
        print("No match found")
        return None
    match_coordinates = []
    for pt in zip(*loc[::-1]):
        adjusted_pt = (pt[0] + 40, pt[1] - 40)
        match_coordinates.append(adjusted_pt)
        cv2.rectangle(img, adjusted_pt, (adjusted_pt[0] + w, adjusted_pt[1] + h), (0, 255, 0), 2)
    cv2.imwrite('result.png', img)
    print("Coordinates of matches found (adjusted): ", match_coordinates)
    return match_coordinates

match_template('utils\openCV\PC\Image.png', 'utils\openCV\PC\Template.png')
