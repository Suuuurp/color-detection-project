import cv2
import numpy as np
import pandas as pd
from PIL import Image

# Load color dataset
csv_path = "colors.csv"
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv(csv_path, names=index, header=None)

def get_color_name(R, G, B):
    """Find the closest color name from the dataset."""
    min_dist = float("inf")
    cname = "Unknown"
    hex_val = "#000000"
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = csv.loc[i, "color_name"]
            hex_val = csv.loc[i, "hex"]
    return cname, hex_val

def detect_color(image):
    """Process an image and return detected color information."""
    img = np.array(image)
    height, width, _ = img.shape
    center_x, center_y = width // 2, height // 2
    b, g, r = img[center_y, center_x]
    color_name, hex_value = get_color_name(r, g, b)
    
    return color_name, hex_value, (r, g, b), img
