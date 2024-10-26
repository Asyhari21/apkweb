import streamlit as st

def main_pages():
    st.markdown("# Main page ")
    st.sidebar.markdown("# Main page ")

def page2():
    st.markdown("# Page 2 ")
    st.sidebar.markdown("# Page 2")

def page3():
    st.markdown("# Page 3 ")
    st.sidebar.markdown("# Page 3 ")

page_name_to_funcs = {
    "Main page": main_pages,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_name_to_funcs.keys())
page_name_to_funcs[selected_page]()