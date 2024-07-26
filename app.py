import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_player import st_player
from streamlit_timeline import timeline
import json

# CSS to improve the layout and look of the sidebar and main page
sidebar_css = """
<style>
/* Sidebar radio buttons styling */
.stRadio > div {
    background-color: #E6E6FA; /* Light purple background */
    border-radius: 10px; /* Rounded corners */
    padding: 10px; /* Padding around the options */
}

/* Sidebar radio buttons labels styling */
.stRadio > div > label {
    color: blue; /* Change font color */
}

/* Social icons container */
.social-icons {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Social icon styling */
.social-icon {
    width: 44px;
    height: 44px;
    margin-right: 10px;
}

/* Remove bullet points from list items in the sidebar */
.sidebar .stSidebar > div > div > ul, .sidebar .stSidebar > div > div > ul > li {
    list-style-type: none; /* Remove bullet points */
    padding-left: 0; /* Remove padding */
}
</style>
"""


with st.sidebar:
    # st.markdown(sidebar_css, unsafe_allow_html=True)
    st.markdown("""
<style>
.custom-button {
    border: none;
    color: white;
    padding: 8px 16px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

.green-button {
    background-color: #4CAF50; /* Green */
}
</style>
""", unsafe_allow_html=True)
    selected = 'Home'


    if st.button('Home'):
            selected = 'Home'
    if st.button('Year-in-review'):
            selected = 'Year-in-review'
    if st.button('Honors experiences'):
            selected = 'Honors experiences'
    # Social icons in the sidebar
    st.markdown("""
    <div class="social-icons">
        <a href="https://www.linkedin.com" target="_blank">
            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" class="social-icon">
        </a>
        <a href="https://www.github.com" target="_blank">
            <img src="https://img.icons8.com/material-outlined/48/000000/github.png" class="social-icon">
        </a>
    </div>
    """, unsafe_allow_html=True)

# Main page content based on selected option
if selected == "Home":
    col1, col2 = st.columns(2)
    pdffile = open('Nachiket-Dighe-Resume.pdf', 'rb')
    with col1:
        st.image('Nachi.jpeg', width=350)
    with col2:
        st.markdown('## Nachiket Dighe')
        st.markdown('#### *University Of Cincinnati*')
        st.markdown('##### College of Engineering and Applied Sciences')
        st.markdown('#### Computer Science and Software Engineering')
        st.download_button('My Resume', pdffile, file_name='Nachiket-Dighe-Resume.pdf', mime='pdf')

    st.markdown("---")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('## About Me')
        st.markdown('Hi my name is Nachi! I am a fourth year majoring in Computer science with a minor in software engineering at the University of Cincinnati. I currently work as a data scientist for Delta Air Lines.')
        st.markdown('I enjoy being challenged technically, and work on projects that involve data science and Artificial intelligence')

    with col4:
        st.image('Nachi1.jpeg', width=350)
    
    st.markdown("---")
    st.markdown('## My Career timeline')
    with open('timeline.json', "r") as f: 
       data = json.load(f)
    timeline(data, height=500)
    
    st.markdown("---")
    col5, col6 = st.columns(2)
    with col5:
        st.image('Nachi3.jpeg')
    with col6:
        st.markdown('## My involvements')
        st.markdown(' - CEAS Ambassadors ')
        st.markdown(' - Student Orientation Leader ')
        st.markdown(' - Honors Peer Leader ')

elif selected == "Year-in-review":
    st.markdown("<div style='text-align: center; font-size: 32px;'>Year-in-review</div>", unsafe_allow_html=True)    
    st.image('Nachi6.jpeg')
    filename = 'text.txt'

# Read the file contents
    with open(filename, 'r') as file:
        file_contents = file.read()

    # Use st.markdown to display the file contents within a styled div
    # Adjust the max-height as needed to fit your screen size
    st.markdown(f"""
        <div style="white-space: pre-wrap; word-wrap: break-word; max-height: 800px; overflow-y: hidden;">
            {file_contents}
        </div>
        """, unsafe_allow_html=True)
    # st.markdown("For my year in review, I woudl like to talk about what experience had the most effect one me last year wasn an acting class I took for my fall semester.")
    # st_player("https://youtu.be/CmSKVW1v0xM")

elif selected == "Honors experiences":    
    st.markdown("# Honors experiences")
    col5, col6 = st.columns(2)
    with col5:
        st.image('Nachi4.jpeg')
    with col6:
        st.markdown('## Student Orientation Leader')
        st.markdown('2021')
        st.markdown(' - Represent the University by providing campus tours, responding to inquiries via email, and assisting incoming first-year students.')
    
    st.markdown("---")
    col7, col8 = st.columns(2)
    with col7:
        events = [
    {"date": "2024-02-14", "event": "Valentines Card Making: Card Making event for Valentines day to Loved Ones"},
    {"date": "2024-03-16", "event": "Women's History Month Jeapordy: Invited other Honor students to enjoy a jeopardy themed game for Women's history Month"},
    {"date": "2024-01-21", "event": "Transition Student Welcome Day"},
]

        st.markdown('## Honors Belong Coordinator')
        st.markdown('2023')
        st.markdown(' - Foster awareness and inclusivity among Honors students by interactive educational programming.') 

    with col8:
        st.image('Nachi5.jpeg')