import streamlit as st
from datetime import datetime

st.title("st.cache의 중요성")
# @st.cache_data # 이것이 있냐 없냐에 따라 실행 속도가 달라져요! 
def print_time():
    # 앱을 실행할 때마다 현재 시간이 표시됩니다.
    now = datetime.now()
    return now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")

# 함수 실행
st.write("현재 시각은", print_time(), "입니다.")


your_text = st.text_input("텍스트를 입력하세요. ")
st.write(your_text+"라고 입력하셨네요!")

if st.button('click!'):
    st.balloons()