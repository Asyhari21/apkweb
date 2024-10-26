import streamlit as st

col1, col2, col3, col4 = st.columns(4)
col1.metric("temperature", "25 °C", "1.2 °C")
col2.metric("Wind", " 9 kph", "-8%")
col3.metric("humidty", "86%", "4%")
col4.metric("Rain", "1.6mm")