import streamlit as st
import scripts.st_better_img as stimg
def top_line():
    tab1, tab2, tab3 = st.tabs(["🎂我的主页", "🍰我的研究", "🍭我的应用"])

def my_cv():
    with st.container():
        cols = st.columns(3)
        with cols[0]:
            stimg.render_svg('src/svg/icon.svg',width="50")
        with cols[1]:
            st.markdown("## FreedomFrank")
        st.code("https://github.com/cnsdqd-dyb")

def left_right():
    text,img = st.columns(2)
    with text:
        st.markdown("# 有朋自远方来，不亦说乎！")
        st.caption("## Welcome my friend!")
    with img:
        #stimg.render_svg('src/svg/1876.svg')
        stimg.load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_0jQBogOQOn.json')

def self_intro():
    st.title("关于我的爱好和特长！")
    img2,text2 = st.columns(2)
    with img2:
        stimg.render_svg('src/svg/3D Guy.svg', shadow=False, width='50')
    with text2:
        with st.container():
            st.caption("## 足球爱好者")
            with st.expander("足球爱好者"):
                st.caption("more ...")
            st.caption("## 音乐爱好者")
            with st.expander("音乐爱好者"):
                st.caption("more ...")
            st.caption("## 游戏制作爱好者")
            with st.expander("游戏制作爱好者"):
                st.caption("more ...")
            st.caption("## 人工智能研究者")
            with st.expander("人工智能研究者"):
                st.caption("more ...")