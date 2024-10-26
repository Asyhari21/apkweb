import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Memuat data
data = pd.read_csv('./data.csv')
data_score = pd.read_csv('./data_score.csv')

# Menggabungkan kedua dataframe berdasarkan 'id'
merged_data = pd.merge(data, data_score, on='id')



def main():
    st.sidebar.title("Adjektif Sentimen Analisis")
    menu = ["Home", "Data"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Sentimen Analisis Bahasa Indonesia")
        words = st.text_input("Masukan Kata:")
        if st.button("Analisis"):
            st.write(words)
            st.write("Hasil Sentimen Analisis:")
            st.write(sentiment_analysis(words))
    elif choice == "Data":
        Data()
    
    
    



def sentiment_analysis(words):
    # Menghitung jumlah kata
    word_count = len(words.split())

    # Menghitung jumlah karakter
    char_count = len(words)

    # Menghitung jumlah huruf kapital
    upper_count = len([word for word in words.split() if word.isupper()])

    # Menghitung jumlah kata unik
    unique_count = len(set(words.split()))

    # Menghitung rasio huruf kapital terhadap jumlah kata
    upper_ratio = upper_count / word_count

    # Menghitung rasio kata unik terhadap jumlah kata
    unique_ratio = unique_count / word_count

    # Menghitung score sentimen
    score = calculate_sentiment_score(words)

    # Kategorisasi sentimen berdasarkan
    sentiment = categorize_sentiment(score)

    return {
        'word_count': word_count,
        'char_count': char_count,
        'upper_count': upper_count,
        'unique_count': unique_count,
        'upper_ratio': upper_ratio,
        'unique_ratio': unique_ratio,
        'score': score,
        'sentiment': sentiment
    }


def calculate_sentiment_score(words):
    # Memuat kamus sentimen
    sentiment_words = merged_data

    # Menghitung score sentimen
    score = 0
    for word in words.split():
        if word in sentiment_words['word'].values:
            score += sentiment_words.loc[sentiment_words['word'] == word, 'score'].values[0]
    return score

# Kategorisasi sentimen berdasarkan score
def categorize_sentiment(score):
    if score > 0:
        return 'Positif'
    elif score < 0:
        return 'Negatif'
    else:
        return 'Netral'




def Data():
    st.markdown("Data")
    # Menambah kolom 'sentiment' berdasarkan score
    merged_data['sentiment'] = merged_data['score'].apply(categorize_sentiment)

    # Menghitung jumlah sentimen
    sentiment_count = merged_data['sentiment'].value_counts()

    # Menampilkan tabel data yang sudah digabungkan
    st.write("Data Gabungan")
    st.dataframe(merged_data)

    # Menampilkan diagram batang untuk visualisasi sentimen
    st.write("Visualisasi Sentimen")
    fig, ax = plt.subplots()
    sentiment_count.plot(kind='bar', ax=ax, color=['green', 'gray', 'red'])
    ax.set_xlabel("Kategori Sentimen")
    ax.set_ylabel("Jumlah")
    ax.set_title("Distribusi Sentimen")
    st.pyplot(fig)

    

if __name__ == '__main__':
    main()