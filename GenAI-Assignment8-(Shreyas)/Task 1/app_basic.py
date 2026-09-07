import streamlit as st
st.write('Welcome To Streamlit!')
name = st.text_input('Enter Your Name')
if st.button('Greet Me'):
    st.write(f'Hello,{name}')
