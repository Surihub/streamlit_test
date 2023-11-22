import streamlit as st
from datetime import datetime

# Streamlit 앱의 제목을 설정합니다.
st.title("20120401는 몇요일인가요?")

# 요일을 한글로 변환하는 함수입니다.
def get_day_of_week_korean(date_obj):
    days_in_korean = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    # datetime 객체의 weekday() 메소드는 월요일을 0, 일요일을 6으로 반환합니다.
    return days_in_korean[date_obj.weekday()]

# 사용자로부터 날짜 입력을 받습니다. 여덟 자리 숫자 형태로 입력받습니다 (예: 20231110).
date_input = st.text_input("날짜를 입력하세요 (YYYYMMDD)", "")

# 입력된 날짜가 올바른 형식인지 확인합니다.
if date_input and len(date_input) == 8:
    try:
        # 문자열을 날짜 객체로 변환합니다.
        date_object = datetime.strptime(date_input, '%Y%m%d')
        # 한글 요일을 찾습니다.
        day_of_week_korean = get_day_of_week_korean(date_object)
        # 결과를 화면에 출력합니다.
        st.write(f"## {date_input}는 {day_of_week_korean}입니다.")
    except ValueError:
        # 입력된 날짜가 올바르지 않은 경우 사용자에게 오류 메시지를 표시합니다.
        st.error("유효한 날짜를 YYYYMMDD 형식으로 입력해주세요.")
else:
    # 입력되지 않았거나 입력 길이가 맞지 않을 경우 메시지를 표시합니다.
    st.write("지정된 형식으로 날짜를 입력해주세요.")
