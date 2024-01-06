"""
----- Portfolio Homepage -----
Contains the code to homepage of the portfolio website.
Homepage contains the introduction to the website and 
directions to all the other pages/features.
"""

import os
import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from st_pages import hide_pages
import webbrowser
from script import *

if __name__ == "__main__":

    # Fetching env variables
    TOKEN = os.environ["AIRTABLE_API_KEY"]
    BASEID = os.environ["BASEID"]

    # Setting the page configurations
    st.set_page_config(
        page_title="Portfolio",
        layout="wide"
    )
    # Hiding pages from sidebar menu
    hide_pages(["Resume", "Email"])
    
    # Top container
    with st.container():
        st.image("asset/img/Top_Banner.png")
    st.divider()

    # Sidebar contact info
    with st.sidebar:
        selected = option_menu(
            "Get in touch", [None, "LinkedIn", "GitHub", "Email"],
            icons=[" ", "linkedin", "github", "envelope"], 
            menu_icon="phone",
            styles={
                "nav-link" : {"--hover-color" : "#d080f2"},
                "nav-link-selected" : {"background-color" : "#ab0af0"}
            }
        )

        if selected == "LinkedIn":
            webbrowser.open_new_tab("https://www.linkedin.com/in/raveesh-yadav/")
        elif selected == "GitHub":
            webbrowser.open_new_tab("http://github.com/Raveesh1505")
        elif selected == "Email":
            switch_page("Email")
        
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
                st.button("Machine Learning")
                st.button("Data Analysis/Visualisation")
            with sub_column7:
                st.button("Map Reduce")
                st.button("OOP")

    # Projects container
    with st.container(border=True):
        st.header("Projects")
        project_tab1, project_tab2, project_tab3 = st.tabs(["Slide 1", "Slide 2", "View all projects"]) 

        # Slide 1 for projects
        with project_tab1:
            # Columns for each
            p1_column1, p1_column2, p1_column3 = st.columns(3)
            with p1_column1:
                st.image("asset/img/proj/Spotify.png")
                st.header("Spotify Recommendations")
                st.markdown("Spotify recommendations using machine learning and PySpark. Analyses song taste using ML model and predicts the likeability of any song entered.")
                st.link_button("View project", "https://github.com/Raveesh1505/Spotify-recommendations")

            with p1_column2:
                st.image("asset/img/proj/Discord.png")
                st.header("Sentinel-Discord Bot")
                st.markdown("Sentinel is a powerful, efficient and fully secure password managing Discord Bot! With password being stored as Cypher-text, sentinel assures a secure environment for your password storage.")
                st.link_button("View project", "https://github.com/sentinel-pw/sentinel-discord")

            with p1_column3:
                st.image("asset/img/proj/Mapreduce.png")
                st.header("Map Reduce Programs")
                st.markdown("Problems solved using MapReduce model. Solved problems of titanic prediction and odd even prediction of a number entered by the user.")
                st.link_button("View project", "https://github.com/Raveesh1505?tab=repositories&q=Mapreduce-&type=&language=&sort=")

        # Slide 2 for projects
        with project_tab2:
            # Columns for each
            p2_column1, p2_column2, p2_column3 = st.columns(3)
            with p2_column1:
                st.image("asset/img/proj/Cricket.png")
                st.header("CricBot-Discord Bot")
                st.markdown("Cricbot is a game bot for Discord that plays cricket with the user.")
                st.link_button("View project", "https://github.com/Raveesh1505/CricBot")

            with p2_column2:
                st.image("asset/img/proj/Clock.png")
                st.header("Clock using Python")
                st.markdown("Clock app using Python with various features like stopwatch, timer and alarm")
                st.link_button("View project", "https://github.com/Raveesh1505/clock")

            with p2_column3:
                st.image("asset/img/proj/Football.png")
                st.header("Football prediction")
                st.markdown("Prediction for qulification of a certain football team after a major shakeup in the lineup using machine learning. Collected historical data using web scrapping.")
                st.link_button("View project", "https://github.com/Raveesh1505/Football-Prediction")

        with project_tab3:
            # Display all projects using airtable
            with st.spinner("Loading all current projects"):
                projectsData = read_airtable(TOKEN, BASEID, "Projects")
            st.dataframe(
                data=projectsData,
                column_config={
                    "Link" : st.column_config.LinkColumn(
                        "Github Link"
                    )
                },
                column_order=("Project", "Link", "Notes")
            )