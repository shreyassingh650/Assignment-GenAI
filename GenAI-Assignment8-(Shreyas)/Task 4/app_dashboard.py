import streamlit as st
sales = {
    'January': 1200,
    'February': 1500,
    'March': 900,
    'April': 2000
}
st.title('Simple Sales Dashboard')
st.text('This is Streamlit Dashboard')
month = st.selectbox('Months',['January','February','March','April'])
st.write(sales.get(month))
st.bar_chart(sales)

