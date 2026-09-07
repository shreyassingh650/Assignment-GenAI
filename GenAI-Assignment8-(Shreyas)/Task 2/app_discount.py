import streamlit as st
product_price=st.text_input('Product Price')
discount_percentage=st.slider("Discount Percentage",1,50,5)
if st.button('Calculate Price'):
    price = int(product_price)
    final_price=price-price*discount_percentage/100
    st.success(final_price)
    #optional
    st.table([["Before", "After"],
          [product_price, final_price]])