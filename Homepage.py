"""
----- Portfolio Homepage -----
Contains the code to homepage of the portfolio website.
Homepage contains the introduction to the website and 
directions to all the other pages/features.
"""

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Setting the page configurations
st.set_page_config(
    page_title="Portfolio",
    layout="wide",
)
# Top container
with st.container():
    top_column_1, top_column_2 = st.columns([4,1.5])
    with top_column_1:
        st.title("Hi, I'm :blue[Raveesh Yadav!]")
        st.subheader("Tech students and an aspirant :blue[Data Engineer]")
        
    with top_column_2:
        st.image("asset/img/self_img.PNG", width=250)
st.divider()

# Sidebar contact info
with st.sidebar:
    st.title('Contact info')
    st.link_button("LinkedIn", 'https://www.linkedin.com/in/raveesh-yadav/')
    st.link_button("Github", 'http://github.com/Raveesh1505')
    if st.button("Email"):
        st.success("Email at: raveeshyadav8@outlook.com")

# About me container
with st.container(border=True):
    st.header("About me")
    st.markdown("I am tech student and an aspirant Daa Engineer who holds a strong command over **Python programming**. I started working using Python during my high school years and have always been fascinated by the simplicity of this language. Though it seems to be simple, the true potential of this language lies beneath the diversified use it provides and one can express their skills with no boundaries using it. I am also fluent in SQL and have keen interest in machine learning.\n\nI hope to be a fruit to this industry and bring smiles on the faces of people I come across!")
    
    if st.button("View and donwload resume"):
        switch_page("Resume")

# Certifications container
with st.container(border=True):
    st.header("Certifications")
    certi_column1, certi_column2, certi_column3 = st.columns(3)
    with certi_column1:
        st.image("asset/img/certi/pcep.png", width=250)
        st.subheader("PCEP")

    with certi_column2:
        st.image("asset/img/certi/GoldMan.png", width=350)
        st.subheader("Goldman")

    with certi_column3:
        st.image("asset/img/certi/AWS-Cloud.png", width=250)
        st.subheader("AWS")

    if st.button("View all certifications"):
        switch_page("Certifications")

# Projects container
with st.container(border=True):
    st.header("Projects")
    st.markdown("Projects container")
    if st.button("View all projects"):
        switch_page("Projects")