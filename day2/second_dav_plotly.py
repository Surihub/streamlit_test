# Plotly와 Streamlit을 사용한 데이터 시각화 애플리케이션
import plotly.express as px  # Plotly Express를 불러옵니다.
import streamlit as st  # Streamlit 라이브러리를 불러옵니다.

st.title("plotly를 활용한 데이터 시각화")

st.subheader("gapminder 데이터")
# 데이터 준비: Plotly Express의 내장 데이터셋인 gapminder를 불러옵니다.
df = px.data.gapminder()

# 산점도 그래프를 생성합니다. 2007년 데이터에 대해 국가별 GDP, 기대 수명 등을 시각화합니다.
fig = px.scatter(
    df.query("year==2007"),  # 2007년 데이터만 필터링합니다.
    x="gdpPercap",  # x축은 1인당 GDP
    y="lifeExp",  # y축은 기대 수명
    size="pop",  # 점의 크기는 인구수를 기준으로 합니다.
    color="continent",  # 색상은 대륙별로 구분합니다.
    hover_name="country",  # 마우스 오버시 나라 이름을 표시합니다.
    log_x=True,  # x축은 로그 스케일로 표시합니다.
    size_max=60,  # 점의 최대 크기를 설정합니다.
)

# Streamlit의 탭 기능을 사용하여 두 가지 테마 옵션을 제공합니다.
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Streamlit 테마를 적용한 그래프를 표시합니다.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Plotly 기본 테마를 적용한 그래프를 표시합니다.
    st.plotly_chart(fig, theme=None, use_container_width=True)

st.subheader("붓꽃 데이터 시각화")  # 사용자 정의 컬러스케일을 정의하는 부분입니다.

# 새로운 데이터셋 (아이리스 데이터) 로드
df = px.data.iris()

# 산점도 그래프를 생성합니다. 이번에는 아이리스 데이터셋을 사용합니다.
fig = px.scatter(
    df,
    x="sepal_width",  # x축은 꽃받침의 너비
    y="sepal_length",  # y축은 꽃받침의 길이
    color="sepal_length",  # 색상은 꽃받침 길이에 따라 변합니다.
    color_continuous_scale="reds",  # 연속적인 색상 스케일로 'reds'를 사용합니다.
)

# 다시 두 가지 테마 옵션을 가진 탭을 생성합니다.
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Streamlit 테마를 적용한 그래프를 표시합니다.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Plotly 기본 테마를 적용한 그래프를 표시합니다.
    st.plotly_chart(fig, theme=None, use_container_width=True)
