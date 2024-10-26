import streamlit as st

# Callback function yang akan dipanggil saat ada perubahan pada slider atau checkbox
def form_callback():
    st.write(f"Slider value: {st.session_state.my_slider}")
    st.write(f"Checkbox value: {st.session_state.my_checkbox}")

# Membuat form
with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)