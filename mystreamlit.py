import streamlit as st

st.image('./pic/011.jpg')
col1,col2 = st.columes(2)

with col1:
    st.header('ต่อตระกูล สุขปาน')
with col2:
    st.subheader('วิทยาการข้มูล')
    st.text('คณะวิทยาศาสตร์และเทคโนโลยี')

st.header('Tortakoon Sukpan')