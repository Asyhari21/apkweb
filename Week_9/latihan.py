import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Fungsi untuk memuat model dari file PKL
def load_model():
    try:
        with open('score.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("File 'score.pkl' tidak ditemukan. Pastikan file tersebut ada di direktori yang benar.")
        return None
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat model: {e}")
        return None

# Muat model
model = load_model()

# Set judul aplikasi dengan styling
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #4CAF50;
        font-size: 32px;
        font-weight: bold;
    }
    .description {
        font-size: 20px;
        text-align: center;
        color: #333;
        margin-bottom: 30px;
    }
    .slider-label {
        font-size: 16px;
        margin-bottom: 10px;
        text-align: center;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #777;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Aplikasi Prediksi Nilai Ujian</div>', unsafe_allow_html=True)

# Menu Navigasi
menu = st.sidebar.selectbox("Pilih Menu", ["Prediksi Nilai Ujian", "Visualisasi Prediksi"])

# Cek apakah model berhasil dimuat
if model is not None:
    if menu == "Prediksi Nilai Ujian":
        st.markdown('<div class="description">Prediksi nilai ujian berdasarkan jam belajar menggunakan model regresi linier.</div>', unsafe_allow_html=True)

        # Input dari pengguna
        hours = st.slider('Masukkan jumlah jam belajar (jam):', 0.0, 10.0, 1.0, step=0.1)

        # Button prediksi
        if st.button('Prediksi Nilai'):
            predicted_score = model.predict(np.array([[hours]]))
            st.write(f'**Jumlah Jam Belajar:** {hours:.1f} jam')
            st.write(f'**Prediksi Nilai Ujian:** {predicted_score[0]:.2f}')

    elif menu == "Visualisasi Prediksi":
        st.markdown('<div class="description">Visualisasi hubungan antara jam belajar dan prediksi nilai ujian.</div>', unsafe_allow_html=True)
        
        # Membuat data contoh untuk visualisasi
        example_hours = np.arange(0, 10, 0.1).reshape(-1, 1)
        predicted_scores = model.predict(example_hours)

        # Plot hasil regresi
        fig, ax = plt.subplots()
        ax.scatter(example_hours, predicted_scores, color='blue', label='Prediksi', alpha=0.6)
        ax.plot(example_hours, predicted_scores, color='red', label='Regresi')
        ax.set_title('Hubungan Jam Belajar dan Prediksi Nilai', fontsize=16)
        ax.set_xlabel('Jam Belajar', fontsize=14)
        ax.set_ylabel('Prediksi Nilai Ujian', fontsize=14)
        ax.legend()

        # Tampilkan visualisasi
        st.pyplot(fig)

    # Footer Aplikasi
    st.markdown("""
    <div class="footer">
        Dibuat dengan menggunakan ❤️
    </div>
    """, unsafe_allow_html=True)

else:
    st.stop()  # Hentikan eksekusi jika model gagal dimuat