import streamlit as st
import os


def set_page_title(title):
    st.sidebar.markdown(unsafe_allow_html=True, body=f"""
        <iframe height=0 srcdoc="<script>
            const title = window.parent.document.querySelector('title') \

            const oldObserver = window.parent.titleObserver
            if (oldObserver) {{
                oldObserver.disconnect()
            }} \

            const newObserver = new MutationObserver(function(mutations) {{
                const target = mutations[0].target
                if (target.text !== '{title}') {{
                    target.text = '{title}'
                }}
            }}) \

            newObserver.observe(title, {{ childList: true }})
            window.parent.titleObserver = newObserver \

            title.text = '{title}'
        </script>" />
    """)


def read(path):
    if not os.path.exists(path):
        write(path, '')
    with open(path, 'r') as f:
        t = f.read()
        print(t)
        f.close()
    return t
def add(path,str):
    if not os.path.exists(path):
        write(path,'')
    with open(path, 'a') as f:
        f.write(str)
        f.close()
def clear(path):
    os.remove(path)
def write(path,str):
    with open(path, 'w+') as f:
        f.write(str)
        f.close()