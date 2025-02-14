import streamlit as st

st.set_page_config(page_title="Portfolio", page_icon=":wave:", layout="wide")

about_me = st.Page("pages/about.py", title="About me",
                   icon=":material/dashboard:", default=True)

pg = st.navigation({
    "About me": [about_me]
})

pg.run()
