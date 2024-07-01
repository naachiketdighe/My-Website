import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_player import st_player
from streamlit_timeline import timeline
import json

with st.sidebar:
        st.markdown("""
<style>
/* Target the radio buttons directly */
.stRadio > div {
    background-color: #f0f2f6; /* Light grey background */
    border-radius: 10px; /* Rounded corners */
    padding: 10px; /* Padding around the options */
}

/* Target the label of the radio buttons */
.stRadio > div > label {
    color: green; /* Change font color */
}
</style>
""", unsafe_allow_html=True)

    # Using an expander to create a collapsible sectiont expanded=True to have it expanded by default
        selected = st.radio(
            "Choose a page:",
            options=['Home', 'Year-in-review', 'Honors experiences']
        )
        st.markdown("""
        <div style="display:flex;justify-content:start;align-items:left;">
            <a href="https://www.linkedin.com" target="_blank">
                <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" style="width:24px;height:24px;margin-right:10px;">
            </a>
            <a href="https://www.github.com" target="_blank">
                <img src="https://img.icons8.com/material-outlined/48/000000/github.png" style="width:24px;height:24px;">
            </a>
        </div>
""", unsafe_allow_html=True)

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
    st.markdown("""---""")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('## About Me')
        st.markdown('Hi my name is Nachi! I am a fourth year majoring in Computer science with a minor in software engineering at the University of Cincinnati. I currently work as a data scientist for Delta Air Lines.')
        st.markdown('I enjoy being challenged technically, and work on projects that involve data science and Artificial intelligence')

    with col4:
        st.image('Nachi1.jpeg', width=350)
    
    st.markdown("""---""")
    
    st.markdown('## My Career timeline')
    with open('timeline.json', "r") as f: 
       data = json.load(f)
    timeline(data, height=500)
    
    st.markdown("""---""")

    col5, col6 = st.columns(2)
    with col5:
        st.image('Nachi3.jpeg')
    with col6:
        st.markdown('## My involvements')
        st.markdown(' - CEAS Ambassadors ')
        st.markdown(' - Student Orientation Leader ')
        st.markdown(' - Honors Peer Leader ')

if selected == "Year-in-review":
    st_player("https://youtu.be/CmSKVW1v0xM")

if selected == "Honors experiences":    
    st.markdown("# Honors experiences")
    col5, col6 = st.columns(2)
    with col5:
        st.image('Nachi4.jpeg')
    with col6:
        st.markdown('## Student Orientation Leader')
        st.markdown('2021')
        st.markdown(' - Represent the University by providing campus tours, responding to inquiries via email, and assisting incoming first-year students.')
    
    st.markdown("""---""")

    col7, col8 = st.columns(2)
    with col7:
        events = [
    {"date": "2021-01-01", "event": "Event 1 description"},
    {"date": "2021-02-01", "event": "Event 2 description"},
    {"date": "2021-03-01", "event": "Event 3 description"},
]

# Display the vertical timeline
        for event in events:
            st.markdown(f"### {event['date']}")
            st.write(event['event'])
            st.markdown("---")  # Separator line
        st.markdown('## Honors Belong Coordinator')
        st.markdown('2023')
        st.markdown(' - Foster awareness and inclusivity among Honors students by interactive educational programming.') 
    with col8:
        st.image('Nachi5.jpeg')