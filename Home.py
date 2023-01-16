import streamlit as st
import scripts.st_better_img as stimg
import scripts.st_my_components as st_cp
import scripts.st_temp_scripts as stt
st.set_page_config(
    page_title="Freedom Frank Home Page",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "# This is Freedom Frank's platform"
    }
)
stt.set_page_title('Welcome')
if __name__ == '__main__':
    with st.sidebar:
        st_cp.my_cv()
        stimg.load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_4kmUDEKo63.json')
    st_cp.top_line()
    st_cp.left_right()
