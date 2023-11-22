import streamlit as st
from datetime import datetime

st.title("st.cache의 역할!!!!")

@st.cache_data
def print_time():
    now = datetime.now()
    return now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")

st.write(print_time())

name = st.text_input("이름을 입력해주세요!")
st.write(name)
if st.button('click'):
    st.balloons()
    st.subheader("hello!!!")

st.write() #print

import seaborn as sns

df = sns.load_dataset("penguins")
st.write(df)
st.dataframe(df)
