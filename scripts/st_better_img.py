import base64
import streamlit as st
import requests
import time
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

# @st.cache(allow_output_mutation=True)
def render_svg(svg_path,width="100",shadow=True):
    svg = open(svg_path, 'r', encoding='utf-8').read()
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    if shadow:
        html = r'<img src="data:image/svg+xml;base64,%s" style="border-radius:20px; width:%s%%; box-shadow: 5px 5px 5px rgb(63,87,232);"   />' % (b64,width)
    else:
        html = r'<img src="data:image/svg+xml;base64,%s" style="border-radius:20px; width:%s%%;"   />' % (b64,width)
    st.write(html, unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    st_lottie(r.json(), key=time.time())
    return r.json()

# USE https://lottiefiles.com/web-player
# https://assets4.lottiefiles.com/packages/lf20_mKMcjgVTY6.json
# https://assets7.lottiefiles.com/packages/lf20_4kmUDEKo63.json
# https://assets4.lottiefiles.com/packages/lf20_iVPQC8jyX2.json
# https://assets9.lottiefiles.com/packages/lf20_uZeVpjFav8.json
# https://assets1.lottiefiles.com/datafiles/FdtKCvUPkcgdZEvWnsUbSO4rP3pWUWgZ5rKnG0rF/chinese.json
# https://assets4.lottiefiles.com/packages/lf20_UdYGl0sZDs.json
# https://assets4.lottiefiles.com/packages/lf20_PmGV4skHBv.json
# https://assets4.lottiefiles.com/packages/lf20_0jQBogOQOn.json
# https://assets1.lottiefiles.com/packages/lf20_cmsczshd.json