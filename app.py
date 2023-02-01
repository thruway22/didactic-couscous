import streamlit as st
import pandas as pd

def display_input_widgets(stride):
    locals()['col%s0' % stride], locals()['col%s1' % stride], locals()['col%s2' % stride] = form.columns(3)
    locals()['ticker%s' % stride] = locals()['col%s0' % stride].text_input('ticker%s' % stride, label_visibility='collapsed')
    locals()['share%s' % stride] = locals()['col%s1' % stride].number_input('share%s' % stride, min_value=0, step=1, format='%d', label_visibility='collapsed')
    locals()['target%s' % stride] = locals()['col%s2' % stride].number_input('target%s' % stride, min_value=0.0, step=0.1, format='%.1f', label_visibility='collapsed')
    globals().update(locals()) 

st.title('NextTrade')
uploaded_file = st.file_uploader('Choose a file', type='CSV')

with st.expander('or manually input'):
    ticker_count = st.number_input('Enter number', value=0)
    if ticker_count > 0:
        form = st.form('input_form')
        cola, colb, colc = form.columns(3)
        cola.write('Ticker')
        colb.write('Current Shares (x)')
        colc.write('Target Weight (%)')
        for step in range(ticker_count):
            display_input_widgets(step)
        submitted = form.form_submit_button("Submit")

#placeholder = st.empty()
#with placeholder.container():
#    if submitted and uploaded_file is None:
 #       form2 = st.form('input_form2')
  #      for step in range(ticker_count):
   #             display_input_widgets(step) 
    #    form2.form_submit_button("Submit")



if uploaded_file is None:
  pass
else:
  dataframe = pd.read_csv(uploaded_file)
  st.write(dataframe)
