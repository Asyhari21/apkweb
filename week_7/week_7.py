import streamlit as st
import pandas as pd
import altair as alt
from transformers import pipeline

# Menggunakan model pre-trained untuk sentiment analysis bahasa Indonesia yang sudah di-finetune
sentiment_pipeline = pipeline("sentiment-analysis", model="w11wo/indonesian-roberta-base-sentiment-classifier")

def main():
    # Judul aplikasi
    st.title("Aplikasi Analisis Sentimen Bahasa Indonesia")
    st.subheader("Proyek Streamlit")

    # Sidebar menu
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    # Home Page
    if choice == "Home":
        st.subheader("Home")

        # Form input teks
        with st.form(key="nlpForm"):
            raw_text = st.text_area("Masukkan teks dalam bahasa Indonesia")
            submit_button = st.form_submit_button(label='Analisis')

        # Progress bar untuk proses
        progress = st.progress(0)

        # Cek apakah tombol submit ditekan
        if submit_button:
            st.write("Teks yang diinput:", raw_text)

            # Memastikan input tidak kosong
            if raw_text.strip() != "":
                progress.progress(30)  # Set progress bar
                
                # Proses analisis sentimen
                sentiment_result = sentiment_pipeline(raw_text)
                sentiment = sentiment_result[0]
                st.write(sentiment)  # Tambahkan ini untuk debugging
                
                # Emoji dictionary
                emoji_dict = {
                    "POSITIVE": "😊",
                    "NEGATIVE": "😢",
                    "NEUTRAL": "😐"
                }

                # Dapatkan label sentimen dari hasil analisis
                sentiment_label = sentiment.get('label', 'NEUTRAL')  # Pastikan ada nilai default
                st.markdown(f"**Hasil Sentimen**: {emoji_dict.get(sentiment_label, '😐')}")

                progress.progress(60)  # Update progress bar
                
                # Menampilkan hasil analisis sentimen dengan alert berwarna
                if sentiment_label == "POSITIVE":
                    st.success(f"Sentimen Positif :smiley: dengan skor {sentiment['score']:.4f}")
                elif sentiment_label == "NEGATIVE":
                    st.error(f"Sentimen Negatif :angry: dengan skor {sentiment['score']:.4f}")
                else:
                    st.info(f"Sentimen Netral 😐 dengan skor {sentiment['score']:.4f}")

                # Buat DataFrame untuk visualisasi dengan tipe data yang sesuai
                result_df = convert_to_df(sentiment_label, sentiment['score'])
                st.dataframe(result_df)

                progress.progress(90)  # Update progress bar

                # Visualisasi dengan Altair
                c = alt.Chart(result_df).mark_bar().encode(
                    x='metric',
                    y='value',
                    color='metric'
                )
                st.altair_chart(c, use_container_width=True)

                # Grafik Pie untuk visualisasi sentimen
                pie_data = pd.DataFrame({
                    'sentimen': ['Positif', 'Negatif', 'Netral'],
                    'jumlah': [1 if sentiment_label == 'POSITIVE' else 0,
                               1 if sentiment_label == 'NEGATIVE' else 0,
                               1 if sentiment_label == 'NEUTRAL' else 0]
                })

                st.subheader("Distribusi Sentimen")
                pie_chart = alt.Chart(pie_data).mark_arc().encode(
                    theta='jumlah',
                    color='sentimen',
                    tooltip=['sentimen', 'jumlah']
                )
                st.altair_chart(pie_chart, use_container_width=True)
                
                progress.progress(100)  # Finish progress bar
            else:
                st.warning("Teks tidak boleh kosong! Silakan masukkan teks.")

    # About Page
    else:
        st.subheader("About")
        st.write("Ini adalah aplikasi untuk analisis sentimen teks dalam bahasa Indonesia menggunakan model yang telah dilatih untuk sentiment analysis.")

# Fungsi untuk konversi hasil analisis ke DataFrame dengan tipe data yang tepat
def convert_to_df(label, score):
    # Konversi label menjadi string dan score menjadi float agar kompatibel dengan Arrow
    sentiment_dict = {
        'metric': ['Label Sentimen', 'Skor Sentimen'],
        'value': [str(label), float(score)]  # Pastikan tipe data sesuai
    }
    sentiment_df = pd.DataFrame(sentiment_dict)
    return sentiment_df

if __name__ == '__main__':
    main()