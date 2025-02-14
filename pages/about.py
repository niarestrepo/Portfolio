import streamlit as st

PAGE_TITLE = "Digital CV | Estefanía Restrepo Jaramillo |"
ICON = ":wave:"
NAME = "Estefanía Restrepo Jaramillo"
DESCRIPTION = "Short description about me"
EMAIL = "estefania.restrepo127@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "www.linkedin.com/in/niarestrepo",
    "GitHub": ""
}

col_1, col_2 = st.columns(2, gap="small")
with col_1:
    None
with col_2:
    st.title(NAME)
    st.write(DESCRIPTION)
