import streamlit as st
from PIL import Image
from color_detection import detect_color  # Import the function from color_detection.py

st.title("🎨 Real-Time Color Detection")

# Start webcam
camera = st.camera_input("Capture an image for color detection")

if camera:
    # Convert the image to PIL format
    img = Image.open(camera)

    # Detect color
    color_name, hex_value, rgb_values, processed_img = detect_color(img)

    # Display results
    st.subheader(f"Detected Color: {color_name}")
    st.markdown(f"**HEX:** {hex_value} | **RGB:** {rgb_values}")
    st.image(processed_img, caption="Captured Image", use_column_width=True)

    # Show detected color block
    st.markdown(
        f'<div style="width:100px; height:100px; background-color:{hex_value}; border-radius:10px"></div>',
        unsafe_allow_html=True,
    )
