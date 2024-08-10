#Getting Started with Starplex
import streamlit as st
import numpy as np

st.write('Hello, world!')
age = st.selectbox("Choose your age:", np.arange(18, 66, 1))
