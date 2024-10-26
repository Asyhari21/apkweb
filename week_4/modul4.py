import streamlit as st
import pandas as pd
import numpy as np

# URL untuk dataset Uber
DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

# Fungsi caching untuk memuat data
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis='columns', inplace=True)
    data['date/time'] = pd.to_datetime(data['date/time'])
    return data

# Menampilkan judul aplikasi
st.title('Uber Pickups di NYC')

# Menampilkan teks "Loading data..."
data_load_state = st.text('Loading data...')
data = load_data(10000)  # Membatasi data yang diambil ke 10.000 baris
data_load_state.text('Done! (data loaded using @st.cache)')

# Menampilkan data mentah jika checkbox diaktifkan
if st.checkbox('Tampilkan data mentah'):
    st.subheader('Data mentah')
    st.write(data)

# Membuat histogram jumlah penjemputan berdasarkan jam
st.subheader('Jumlah penjemputan per jam')
hist_values = np.histogram(data['date/time'].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Membuat peta interaktif berdasarkan waktu pemilihan penjemputan
st.subheader('Peta penjemputan Uber berdasarkan waktu')
hour_to_filter = st.slider('Jam', 0, 23, 17)  # Slider untuk memilih jam
filtered_data = data[data['date/time'].dt.hour == hour_to_filter]
st.map(filtered_data)