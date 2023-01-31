import streamlit as st
import pandas as pd

st.title('NextTrade')
uploaded_file = st.file_uploader("Choose a file", type='CSV')
dataframe = pd.read_csv(uploaded_file)
st.write(dataframe)
