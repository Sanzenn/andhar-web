import streamlit as st
import numpy as np
from PIL import Image
st.write("Image")
image1= Image.open("Andhar.jpg")
st.image(image1)


audio_file = open ('bang al bang al @naplive7.mp3','rb')
audio_bytes =audio_file.read()
st.write("Audio")
st.audio(audio_bytes,format ='bang al bang al @naplive7.mp3')
