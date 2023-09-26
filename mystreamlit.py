import streamlit as st

st.image('./pic/011.jpg')
col1,col2 = st.columns(2)

with col1:
    st.header('ต่อตระกูล สุขปาน')
with col2:
    st.subheader('วิทยาการข้มูล')
    st.text('คณะวิทยาศาสตร์และเทคโนโลยี')

st.header('Tortakoon Sukpan')

html_1 = """
<div style="background-color:#33FF00;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้เบื้องต้น</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd
dt=pt.read_csv('./data/iris.csv')
st.write(dt.head(10))
st.button('show bar chart')