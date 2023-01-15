import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.markdown("about me")
