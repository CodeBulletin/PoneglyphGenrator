import cv2
import numpy as np

for i in range(32, 126):
    for j in range(i + 1, 127):
        a = cv2.imread(f"C:\\Users\\bmalh\\Desktop\\Projects\\Pycodes\\poneglyph_genrator\\Poneglyph\\Poneglyph_{i}.png")
        b = cv2.imread(f"C:\\Users\\bmalh\\Desktop\\Projects\\Pycodes\\poneglyph_genrator\\Poneglyph\\Poneglyph_{j}.png")
        difference = cv2.subtract(a, b)
        result = not np.any(difference)
        if result is True:
            print(f"Pictures are the same: {i} -> {j}")