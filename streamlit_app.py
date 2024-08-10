import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


@st.cache(ttl=60*5, max_entries=20)
def load_data():
    data = pd.read_csv('https://github.com/4GeeksAcademy/machine-learning-content/blob/master/assets/titanic_train.csv')
    return data

data = load_data()


st.markdown('<style>description{color:blue;}</style>', unsafe_allow_html=True)
st.title('Titanic survival prediction')
st.markdown("<description>The sinking of the Titanic is one of the most infamous shipwrecks in history. " + 
"On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding " +
"with an iceberg. Unfortunately, there weren't enough lifeboats for everyone onboard, resulting in the death of " +
"1502 out of 2224 passengers and crew. While there was some element of luck involved in surviving, it seems some " +
"groups of people were more likely to survive than others. </description>", unsafe_allow_html=True)
st.sidebar.title('Select the parameters to analyze survival prediction')
