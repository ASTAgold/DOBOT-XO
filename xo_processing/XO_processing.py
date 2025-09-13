import cv2
import numpy as np

def contenu_cell(cells):
    """
    Analyse each cell image to guess if it contains 'X', 'O', or is empty.
    Returns a list of strings (one label per cell).
    """
    results = []
    for cell in cells:
        gray = cv2.cvtColor(cell, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

        ink_pixels = cv2.countNonZero(thresh)
        total_pixels = thresh.shape[0] * thresh.shape[1]
        ink_ratio = ink_pixels / total_pixels

        if ink_ratio < 0.05:
            label = 'empty'
        else:
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            circularity = 0
            if contours:
                c = max(contours, key=cv2.contourArea)
                perimeter = cv2.arcLength(c, True)
                area = cv2.contourArea(c)
                if perimeter > 0:
                    circularity = 4 * np.pi * area / (perimeter * perimeter)
            if 0.5 < circularity < 1.2:
                label = 'O'
            else:
                label = 'X'

        results.append(label)
    return results

def split_into_cells(image):
    h, w = image.shape[:2]  
    cell_height = h // 3
    cell_width = w // 3
    cells = []

    for i in range(3):
        for j in range(3):
            y1 = i * cell_height
            y2 = (i + 1) * cell_height
            x1 = j * cell_width
            x2 = (j + 1) * cell_width
            cell = image[y1:y2, x1:x2]  
            cells.append(cell)

    return cells
cv2.waitKey(0)
cv2.destroyAllWindows()
