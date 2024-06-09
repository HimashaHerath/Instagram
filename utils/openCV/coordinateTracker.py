import cv2
import numpy as np

def match_template(image_path, template_path):
    # Load the images in grayscale
    img = cv2.imread(image_path, 0)
    template = cv2.imread(template_path, 0)

    # Dimensions of the template
    w, h = template.shape[::-1]

    # Template matching
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # Check if any matches found
    if not loc[0].size:
        print("No match found")
        return None

    # List to store the coordinates of the matches
    match_coordinates = []

    # Draw rectangles around matches
    for pt in zip(*loc[::-1]):  # Adjust coordinates
        match_coordinates.append(pt)
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

    # Save and display results
    cv2.imwrite('result.png', img)

    # Print the coordinates of the matches
    print("Coordinates of matches found: ", match_coordinates)
    return match_coordinates

# Example usage
match_template('image.png', 'Template.png')
