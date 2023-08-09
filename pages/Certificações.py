from streamlit_image_select import image_select
import streamlit as st
import os
st.markdown("# Selecione um certificado para ampliá-lo")
img = image_select(
    label="",
    images = ["assets/certs/"+f for f in os.listdir("assets/certs")],
    captions=None,
    return_value="original"
)
st.write(img)
st.write()
st.image(img)