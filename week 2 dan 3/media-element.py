import streamlit as st

# Media Elements st.image
# Import modul Image dari Python Imaging Library
from PIL import Image
image = Image.open('C:\Streamlit\photo\gunung.jpg')
st.image(image, caption= 'Pemandangan yang indah di gunung')

# Media Element st.audio
audio_file = open('C:\Streamlit\sound\sound.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

# Media Element st.video
video_file = open('C:\Streamlit\clip\water.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)