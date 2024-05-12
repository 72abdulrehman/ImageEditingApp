import streamlit as st
from PIL import Image

st.subheader("Image Editor")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)

    gray_img = img.convert("L")

    st.image(gray_img)
    

uploaded_image = st.file_uploader("uploaded_image")
if uploaded_image:
    img1 = Image.open(uploaded_image)
    gray_img1 = img1.convert("L")
    st.image(gray_img1)