"""
----- Resume Page -----
Contains the code to resume page of the portfolio website.
Resume page contains the work experience and education detials
with an option to donload the PDF format of the resume.
"""

import streamlit as st

with st.container():
    st.image("asset/img/Resume-Banner.png")
st.divider()

# Sidebar contact info
with st.sidebar:
    st.title('Contact info')
    st.link_button("LinkedIn", 'https://www.linkedin.com/in/raveesh-yadav/')
    st.link_button("Github", 'http://github.com/Raveesh1505')
    if st.button("Email"):
        st.success("Email at: raveeshyadav8@outlook.com")

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