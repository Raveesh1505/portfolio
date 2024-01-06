"""
----- Resume Page -----
Contains the code to resume page of the portfolio website.
Resume page contains the work experience and education detials
with an option to donload the PDF format of the resume.
"""

import streamlit as st
import webbrowser
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from st_pages import hide_pages

with st.container():
    st.image("asset/img/Resume-Banner.png")
st.divider()

# Hiding pages from sidebar menu
hide_pages(["Resume", "Email"])

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

# Tabs for different features
tab1, tab2, tab3 = st.tabs(["Work Experience", "Education History", "Download Resume"])

# Work experince
with tab1:
    with st.container(border=True):
        st.header("Intern Data Analayst at M3Bi India Private Ltd.")
        st.caption("Decemeber 2023 - January 2024")
        st.markdown("1. Used SQL to extract data from relational database. The extracted data was used for analysis.\n2. Performed EDA on extracted data to find out useful insights using Python and it's various libraries.\n3. Created necessary dashboards on Tableau to visualise the analysis.")

        st.divider()

# Education backgrounds
with tab2:
    with st.container(border=True):
        st.header("B.Tech in Computer Science")
        st.subheader("The NorthCap University")
        st.caption("2021-2025")
        st.markdown("- Specialed in Data Science.\n- CGPA: 8.0")

        st.divider()

        st.header("All India Sr. School Certificate Examination (AISSCE)")
        st.subheader("Salwan Public School")
        st.caption("2007-2021")
        st.markdown("- Completed grade 12 examination (AISSCE) and grade 10 examination (AISSE).\n- AISSCE Grade: 80%.\n- AISSE Grade: 85.7%")
        
# Download resume
with tab3:
    with open("asset/docs/Raveesh-Resume.pdf", 'rb') as resume:     # PDF read as binary file. Hence need to be read
        st.download_button(
            label="Download PDF format of the resume",
            data=resume,
            file_name="Raveesh_resume.pdf"
        )