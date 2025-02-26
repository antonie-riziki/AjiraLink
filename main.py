import streamlit as st 
import pandas as pd 
import numpy as np 
import seaborn as sb 
import matplotlib.pyplot as plt 
import os
import csv
import sys



registration = st.Page("./pages/registration.py", title="Registration", icon=":material/login:")
home_page = st.Page("./pages/homepage.py", title="Home", icon=":material/house:")
ajirabot = st.Page("./pages/ajirabot.py", title="AjiraBot", icon=":material/chat:")
ajira_ads = st.Page("./pages/ajira-ads.py", title="Ajira Ads", icon=":material/picture_as_pdf:")




pg = st.navigation([registration, home_page, ajira_ads, ajirabot])

st.set_page_config(
    page_title="AJIRALINK",
    page_icon="☣️🚨",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': "# We are a leading insights and predicting big data application, Try *AjiraLink* and experience reality!"
    }
)

with st.sidebar:
    st.markdown('📖 For more similar projects visit [click me](https://www.echominds.africa)!')
    
pg.run()