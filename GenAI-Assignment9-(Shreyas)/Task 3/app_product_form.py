import streamlit as st

name = st.sidebar.text_input('Enter Product Name')
product = st.sidebar.selectbox('Choose',['Electronics','Home Appliances','Cloths'])
price = st.sidebar.number_input('Enter Price')
if st.sidebar.button('Add Product'):
    st.success('Product is Added Success')
    st.table([['Name','Product','Price'],[name,product,price]])
