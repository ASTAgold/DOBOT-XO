import cv2
import numpy as np
from XO_processing import split_into_cells, contenu_cell

image = cv2.imread('board.png')
if image is None:
    print("Error: Could not load image. Make sure 'board.png' is in the same folder.")
    exit()

cells = split_into_cells(image)
statuses = contenu_cell(cells)  # now returns a list like ['X', 'O', 'empty', …]

for idx, (cell, status) in enumerate(zip(cells, statuses)):
    cv2.imshow(f"Cell {idx} ({status})", cell)
    print(f"Cell {idx}: {status}")
    cv2.waitKey(0)
    cv2.destroyWindow(f"Cell {idx} ({status})")

cv2.destroyAllWindows()
