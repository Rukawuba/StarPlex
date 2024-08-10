#Getting Started with Starplex
import streamlit as st
import numpy as np
import altair as alt
import streamlit as st
import pandas as pd


st.write('Hello, world!')
age = st.selectbox("Choose your age:", np.arange(18, 66, 1))
df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c')
st.altair_chart(c, width=-1)
