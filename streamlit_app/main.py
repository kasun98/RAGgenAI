import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
load_dotenv()

from home import run as run_home
from page1 import main as research
from page2 import main as dataai
from page3 import main as chatai
from page4 import run as about

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv('LANGCHAIN_API_KEY')


PAGES = {
    "Home": run_home,
    "Research AI": research,
    "Data AI": dataai,
    "Chat Bot": chatai,
    "About": about,
}
st.set_page_config(page_title="NeuronBit AI Assistant", page_icon=":brain:", layout="wide")
selected2 = option_menu(None, ["Home", "Research AI", "Data AI", "Chat Bot", "About"], 
    icons=['house', 'bi-search', 'bi-graph-up-arrow', 'bi-chat-square-dots', 'bi-people'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "8px", "background-color": "#17202A", "width":"auto", "max-width":"1000px"},
        "icon": {"color": "orange", "font-size": "auto"}, 
        "nav-link": {"font-size": "auto", "text-align": "center", "margin":"0px", "--hover-color": "#4A235A"},
        "nav-link-selected": {"background-color": "#4A235A", "font-weight": "normal"},
    })

if selected2=="Home":
    selection="Home"
if selected2=="Research AI":
    selection="Research AI"
if selected2=="Data AI":
    selection="Data AI"
if selected2=="Chat Bot":
    selection="Chat Bot"
if selected2=="About":
    selection="About"

page = PAGES[selection]
page()

