"""
----- Email Page -----
Contains the code to form to send a query email.
"""

import os
import streamlit as st
from script import send_query_to_airtable
import webbrowser
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from st_pages import hide_pages

# Fetching env variables
TOKEN = os.environ["AIRTABLE_API_KEY"]
BASEID = os.environ["BASEID"]

with st.container():
    st.image("asset/img/Get in touch-Banner.png")

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

with st.container():
    st.markdown("Email at: raveeshyadav8@outlook.com or simple fill the form below:")
    with st.form("Query From", clear_on_submit=True, border=True):
        st.header("Send your query")
        sender_name = st.text_input(
            "Full Name"
        )
        sender_email = st.text_input(
            "Your email address"
        )
        subject = st.text_input(
            "Subject"
        )
        message = st.text_area(
            "Message"
        )

        if st.form_submit_button("Send"):
            queryDetails = {
                "Name" : sender_name,
                "Email" : sender_email,
                "Subject" : subject,
                "Message" : message
            }

            if send_query_to_airtable(TOKEN, BASEID, "Email", queryDetails):
                st.success("Query sent succesfully! Will try to get back shortly.")
            else:
                st.error("Error. Plese try again after refreshing.")