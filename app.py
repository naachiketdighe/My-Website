import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_player import st_player


selected = option_menu(
    menu_title=None,
    options=['Home', 'Year-in-review', 'Honors experiences', ],
    icons=['🍎', '🍊', '🍇'],
    default_index=0,
    orientation='horizontal',
    # styles= {
    #     "nav-link" : {
    #         "--hover-color" : "lightgreen"
    #     }
    # }
)

if selected == "Home":
    col1, col2 = st.columns(2)

    with col1:
        st.image('Nachi.jpeg', width=350)
    with col2:
        st.markdown(' ## Nachiket Dighe')
        st.markdown(' #### *University Of Cincinnati* ' )
        st.markdown(' ##### College of Engineering and Applied Sciences')
        st.markdown(' #####  Computer Science and Software Engineering')
        st.markdown('<style>div.stButton > button:first-child {background-color: blue; color: white; text-align: center;}</style>', unsafe_allow_html=True)
        st.markdown('<div class="stButton"><a href="https://pink-meade-32.tiiny.site/" target="_blank">My Resume</a></div>', unsafe_allow_html=True)
    st.markdown("""---""")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('## About Me')
        st.markdown('Hi my name is Nachi! I am a fourth year majoring in Computer science with a minor in software engineering at the University of Cincinnati. I currently work as a data scientist for Delta Air Lines.')
        st.markdown('I enjoy being challenged technically, and work on projects that innvolve data science and Artificial intelligence')

    with col4:
        st.image('Nachi1.jpeg', width=350)
    
    st.markdown("""---""")

    col5, col6 = st.columns(2)
    with col5:
        st.image('Nachi3.jpeg')
    with col6:
        st.markdown('## My innvolvements')
        st.markdown(' - CEAS Ambassadors ')
        st.markdown(' - Student Oreintation Leader ')
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
        st.markdown(' 2021')
        st.markdown(' - Represent the University by providing campus tours, responding to inquiries via email, and assisting incoming first-year students.')
