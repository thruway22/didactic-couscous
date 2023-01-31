import streamlit as st
import pandas as pd

st.title('NextTrade')
uploaded_file = st.file_uploader("Choose a file", type='CSV')


if uploaded_file is not None:
  pass
else:
  dataframe = pd.read_csv(uploaded_file)
  st.write(dataframe)
