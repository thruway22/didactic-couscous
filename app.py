import streamlit as st
import pandas as pd

st.title('NextTrade')
form = st.form('input_form')
tab1, tab2 = form.tabs(['Upload CSV file', 'Manual input'])
uploaded_file = tab1.file_uploader("Choose a file", type='CSV')
form.form_submit_button("Submit")



if uploaded_file is None:
  pass
else:
  dataframe = pd.read_csv(uploaded_file)
  st.write(dataframe)
