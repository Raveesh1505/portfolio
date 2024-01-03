"""
----- Portfolio Homepage -----
Contains the code to homepage of the portfolio website.
Homepage contains the introduction to the website and 
directions to all the other pages/features.
"""

import streamlit as st
from script import *
from streamlit_extras.switch_page_button import switch_page

# Setting the page configurations
st.set_page_config(
    page_title="Portfolio",
    layout="wide",
)
# Top container
with st.container():
    st.image("asset/img/Top_Banner.png")        
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

# Skills container
with st.container(border=True):
    st.header("Skills and Technologies")
    skill_column1, skill_column2, skill_column3 = st.columns([2,3,2])
    
    # Languages
    with skill_column1:
        st.subheader("Languages")
        sub_column1, sub_column2 = st.columns(2)
        with sub_column1:
            st.button("Python")
            st.button("Java")
            st.button("SQL")
        with sub_column2:
            st.button("C")
            st.button("C++")
            st.button("PigLatin")

    # Tools
    with skill_column2:
        st.subheader("Tools")
        sub_column3, sub_column4, sub_column5 = st.columns(3)
        with sub_column3:
            st.button("Streamlit")
            st.button("Microsoft Azure")
            st.button("Postgres")
        with sub_column4:
            st.button("Hadoop")
            st.button("MySQL")
            st.button("Heroku")
        with sub_column5:
            st.button("Git/GitHub")
            st.button("Visual Studio Code")
            st.button("Airtable")

    # Tools
    with skill_column3:
        st.subheader("Skills")
        sub_column6, sub_column7 = st.columns(2)
        with sub_column6:
            st.button("Big Data")
            st.button("Data Analysis")
            st.button("Data Visualisation")
        with sub_column7:
            st.button("Map Reduce")
            st.button("OOP")

# Projects container
with st.container(border=True):
    st.header("Projects")
    project_tab1, project_tab2 = st.tabs(["Slide 1", "Slide 2"])
    # Columns for each 
    with project_tab1:
        p1_column1, p1_column2, p1_column3 = st.columns(3)
        with p1_column1:
            st.image("asset/img/proj/Spotify.png")
            st.header("Spotify Recommendations")
            st.markdown("REcomends songs for spotify")
            st.link_button("View project", "https://github.com/Raveesh1505/Spotify-recommendations")

        with p1_column2:
            st.image("asset/img/proj/Discord.png")
            st.header("Sentinel-Discord Bot")
            st.markdown("Discord Bot")
            st.link_button("View project", "https://github.com/Raveesh1505/Spotify-recommendations")

        with p1_column3:
            st.image("asset/img/proj/Mapreduce.png")
            st.header("Map Reduce Programs")
            st.markdown("Map Recuce programs")
            st.link_button("View project", "https://github.com/Raveesh1505/Spotify-recommendations")

    with project_tab2:
        p2_column1, p2_column2, p2_column3 = st.columns(3)
        with p2_column1:
            st.image("asset/img/proj/Cricket.png")
            st.header("CricBot-Discord Bot")
            st.markdown("Cricket playing bot")
            st.link_button("View project", "https://github.com/Raveesh1505/Spotify-recommendations")

        with p2_column2:
            st.image("asset/img/proj/Clock.png")
            st.header("Clock using Python")
            st.markdown("Clock with timer, stopwatch etc.")
            st.link_button("View project", "https://github.com/Raveesh1505/Spotify-recommendations")

        with p2_column3:
            st.image("asset/img/proj/Football.png")
            st.header("Football prediction")
            st.markdown("Football prediction")
            st.link_button("View project", "https://github.com/Raveesh1505/Spotify-recommendations")