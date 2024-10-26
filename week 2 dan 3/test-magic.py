import streamlit as st
import pandas as pd

# Data stok barang
data = {
    "Nama Barang": ["Beras", "Gula", "Minyak Goreng", "Telur", "Sabun Mandi", "Pasta Gigi"],
    "Kategori": ["Sembako", "Sembako", "Sembako", "Sembako", "Kebutuhan Rumah", "Kebutuhan Rumah"],
    "Harga": [12000, 14000, 13000, 2000, 3000, 8000],
    "Stok": [50, 80, 60, 100, 40, 30]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame di Streamlit
st.write("Stok Barang Minimarket")
st.dataframe(df)