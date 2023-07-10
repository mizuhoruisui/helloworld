import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'What ar your favolite colors',
    ['Green','Yellow','Red','Blue',
     ['Yellow','Red']])

st.write('You selected:',options)