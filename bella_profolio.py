import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title=f"Bella's Profolio",
    page_icon=':ledger:',
    initial_sidebar_state="expanded",
    layout="wide",
)

def streamlit_menu():
    with st.sidebar:
        selected = option_menu(
            menu_title="Bella Jiang",  # required
            options=["Home", "Data Analysis", "Data Engineering", "Contact"],  # required
            icons=["house", "book", "file-code", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
        )
    return selected
selected = streamlit_menu()

if selected == "Home":
    intro = f"""👋🏻 Hello and welcome to my professional portfolio.
    I am a dedicated Data Analyst transitioning into the realm of Data Engineering, with a robust foundation in engineering principles. My journey in the data world is driven by a profound passion for harnessing the power of data to solve complex problems, improve decision-making processes, and create innovative solutions that drive progress. With a solid background in engineering, I bring a unique blend of technical skills, analytical prowess, and problem-solving capabilities to the table. My experience has equipped me with a deep understanding of both the theoretical and practical aspects of data analysis and engineering, enabling me to design, build, and maintain sophisticated data systems."""
    da_intro = f"""Experienced data analyst with a demonstrated working history in the financial services industry. Creative data storyteller from spreadsheet to code. Skilled in PostgreSQL and Python. Hands-on data visualization and advanced spreadsheet skills."""
    de_intro = f"""As I pivot towards Data Engineering, my goal is to bridge the gap between data analysis and the technical infrastructure that supports it. I am currently deepening my expertise in areas such as database management, cloud computing, big data technologies, and data pipeline construction. My engineering background has been instrumental in this transition, providing me with a strong grasp of the underlying systems and the ability to troubleshoot, optimize, and innovate within complex data environments."""
    hobby_intro = f"""Bushwalking captivates me as my preferred way to spend the weekends, immersing myself in the tranquility and beauty of nature. It\'s an activity that not only rejuvenates my spirit but also challenges my physical limits. This year, I\'ve set myself an ambitious goal: to cover a total of 200 kilometers through hiking."""

    st.title(f"👩🏻‍💻 Introduction")
    st.markdown(intro,unsafe_allow_html=True)

    da_title_font = f"<p style='font-size:20px;'>👩🏻‍🎨 Data Storyteller</p>"
    st.markdown(da_title_font, unsafe_allow_html=True)  
    st.markdown(da_intro)  

    de_title_font = f"<p style='font-size:20px;'>👷🏻‍♀️ Data Architect</p>"
    st.markdown(de_title_font, unsafe_allow_html=True)      
    st.markdown(de_intro)

    hobby_title_font = f"<p style='font-size:20px;'>🥾 Bushwalker</p>"
    st.markdown(hobby_title_font, unsafe_allow_html=True)      
    st.markdown(hobby_intro)
    
if selected == "Projects":
    st.title(f"{selected}")
if selected == "Contact":
    st.title(f"{selected}")