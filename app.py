import streamlit as st
import pandas as pd

st.title('NextTrade')
st.form('input_form')
uploaded_file = form.file_uploader("Choose a file", type='CSV')
form.form_submit_button("Submit")



if uploaded_file is None:
  pass
else:
  dataframe = pd.read_csv(uploaded_file)
  st.write(dataframe)
