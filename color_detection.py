import streamlit as st
import cv2
import numpy as np
import pandas as pd
from PIL import Image

# Load color dataset
csv_path = "colors.csv"
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv(csv_path, names=index, header=None)

def getColorName(R, G, B):
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

st.title("🎨 Real-Time Color Detection")

# Start webcam
camera = st.camera_input("Capture an image for color detection")

if camera:
    # Convert image for OpenCV
    img = Image.open(camera)
    img = np.array(img)

    # Get the center pixel color
    height, width, _ = img.shape
    center_x, center_y = width // 2, height // 2
    b, g, r = img[center_y, center_x]

    # Get color name
    color_name, hex_value = getColorName(r, g, b)

    # Display results
    st.subheader(f"Detected Color: {color_name}")
    st.markdown(f"**HEX:** {hex_value} | **RGB:** ({r}, {g}, {b})")
    st.image(img, caption="Captured Image", use_column_width=True)

    # Show detected color block
    st.markdown(
        f'<div style="width:100px; height:100px; background-color:{hex_value}; border-radius:10px"></div>',
        unsafe_allow_html=True,
    )
