# Design Home Page
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from streamlit_option_menu import option_menu

import json
import requests
import pandas as pd
import numpy as np


from io import StringIO
import langdetect
from langdetect import DetectorFactory, detect, detect_langs
from PIL import Image

st.set_page_config(
    page_title="Streamlit MP5",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.header("Group 11 MP5", divider='rainbow')
# st.sidebar.success("Select a demo case from above")

banner = """
    <body style="background-color:yellow;">
            <div style="background-color:#385c7f ;padding:10px">
                <h2 style="color:white;text-align:center;">Streamlit MP5</h2>
            </div>
    </body>
    """

st.markdown(banner, unsafe_allow_html=True)


st.markdown(
    """
    ###
    #### Genre
    Under Genre kan du få en anbefaling til høje ratede film af samme valgte genre. 
    ### Group 11
    Tobias Carlsen - cph-tc183@cphbusiness.dk

    Christian Kortsen - cph-cc283@cphbusiness.dk

    Daniel Trelborg - cph-dh216@cphbusiness.dk

    Simone Toft Hansen - cph-sh575@cphbusiness.dk
"""
)






