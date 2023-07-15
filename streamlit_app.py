import streamlit as st

st.title('Customiziing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#2E86C1"
secocndaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font"monospace"        
""")

number = st.sidebar.slider('Select a number:',0,10,5)
st.write('Selected number from slider widget is:', number)
