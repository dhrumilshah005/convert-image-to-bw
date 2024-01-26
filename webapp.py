import streamlit as st
from PIL import Image
st.header("Convert an Image to Black and White")
with st.expander("Start Camera"):
    camera_image = st.camera_input("camera")
if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.write("Black and White image")
    st.image(gray_img)
