import streamlit as st
import pandas as pd

# Fungsi caching dengan URL
@st.cache_data
def load_data_from_url(url):
    data = pd.read_csv(url)
    return data

st.title("Latihan penggunaan Caching pada URL Dataset Ketinggian dan Berat Badan")

# Contoh URL dataset
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv'

# Tombol untuk memuat data
if st.button('Muat Data'):
    data = load_data_from_url(url)
    st.write("Data berhasil dimuat dari Dataset Ketinggian dan Berat Badan:")
    st.write(data)