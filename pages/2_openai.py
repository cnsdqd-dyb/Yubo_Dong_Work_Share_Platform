import random
import time

import streamlit as st
import scripts.st_better_img as stimg
import scripts.st_my_components as st_cp

st.set_page_config(
    page_title="Freedom Frank APP OPENAI",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "# This is Freedom Frank's platform"
    }
)

if __name__ == '__main__':
    with st.sidebar:
        st_cp.my_cv()
        stimg.load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_4kmUDEKo63.json')
    st_cp.top_line()

    login = False
    name = st.text_input("用户名")
    if name == 'dyb':
        st.success("欢迎")
        chatui = st_cp.DoubleChatUI(key=name)
        chatui.chat()
    elif name != '':
        st.error("不合法的用户登录!")



