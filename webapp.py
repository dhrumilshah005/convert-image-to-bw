import streamlit as st
from PIL import Image
st.header("Convert an Image to Black and White")
st.write("Please choose either to upload a photo from your computer"
             " or click a new photo")
with st.expander("Upload Image"):
    uploaded_image = st.file_uploader("Upload an Image",key="uploader")
with st.expander("Start Camera"):
    camera_image = st.camera_input("camera",key="camera")
st.button("Convert to B&W",key="button")
st.button("Start again",key="restart")

if "uploader" not in st.session_state:
    st.session_state["uploader"] = 0

if st.session_state["camera"] and st.session_state["button"] :
    uploaded_image = None
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.write("Black and White image")
    st.image(gray_img)
elif st.session_state["uploader"] and st.session_state["button"]:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.write("Black and White image")
    st.image(gray_img)


if st.session_state["restart"]:
    st.session_state["uploader"] += 1
    st.rerun()
    st.session_state.clear()
    st.cache_data.clear()