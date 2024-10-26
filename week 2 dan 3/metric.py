import streamlit as st

st.metric(label="Harga Pertamax", value=4, delta=-0.5)
st.metric(label="Harga Pertamax Turbo", value=7, delta=0.5)
st.metric(label="Jumlah Anak Kucing", value=123, delta=123, delta_color="off")