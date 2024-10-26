import streamlit as st

# Text Element
st.markdown("**Asyhari Tahajjud** :star:")
st.title("Praktikum Aplikasi WEB :smile: :smile:")
st.header("Ini adalah latihan saya :rocket: ")
st.subheader("Prodi Teknologi Informasi")
st.caption("Departemen Pendidikan Teknik Elektronika dab Informatika")
st.text("Saya kuliah sejak tahun 2022")
st.write("NIM saya 22537144001")

# Metric (Turun kebawah)
st.metric(label="Harga Nasi Padang", value=4, delta=-0.5)
st.metric(label="Harga Nasi Goreng", value=7, delta=-0.5)
st.metric(label="Jumlah Anak Sekolah", value=123, delta=123, delta_color="off")

# Column (Ke samping)
col1, col2, col3, col4 = st.columns(4)
col1.metric("temperature", "25 °C", "1.2 °C")
col2.metric("Wind", " 9 kph", "-8%")
col3.metric("humidty", "86%", "4%")
col4.metric("Rain", "1.6mm")

# Magic
import pandas as pd

df= pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [10,20,30,40,50]
})

df

# Latihan Magic
# Data stok barang
import streamlit as st
import pandas as pd

# Data stok barang
data = {
    'Nama Barang': ["Beras", "Gula", "Minyak Goreng", "Telur", "Sabun Mandi", "Pasta Gigi"],
    'Kategori': ["Sembako", "Sembako", "Sembako", "Sembako", "Kebutuhan Rumah", "Kebutuhan Rumah"],
    'Harga': [12000, 14000, 13000, 2000, 3000, 8000],
    'Stok': [50, 80, 60, 100, 40, 30]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame di Streamlit
st.write("Stok Barang Minimarket")
st.dataframe(df)

# Media Element
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