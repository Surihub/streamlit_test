import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Matplotlib로 시각화하기")  # Streamlit 앱의 제목을 설정합니다.

# 선 그래프 생성: Matplotlib의 자유도를 활용하여 선 그래프를 생성합니다.
X = range(0, 100, 10)  # X축 값 설정
Y = [value**2 for value in X]  # Y축 값 설정, X의 각 값에 대해 제곱한 리스트를 생성
fig, ax = plt.subplots()  # 그래프를 그리기 위한 준비
ax.plot(X, Y, 'r*--')  # 빨간색 별표 모양으로 점선을 그립니다.
st.pyplot(fig)  # Streamlit 앱에 그래프를 표시합니다.

# 히스토그램 생성: NumPy를 사용하여 정규 분포에 따른 무작위 데이터를 생성하고 히스토그램을 그립니다.
arr = np.random.normal(1, 1, size=100)  # 평균 1, 표준 편차 1의 정규 분포에서 100개 샘플 추출
fig, ax = plt.subplots()  # 그래프를 그리기 위한 준비
ax.hist(arr, bins=10)  # 데이터를 10개의 구간으로 나누어 히스토그램을 생성
st.pyplot(fig)  # Streamlit 앱에 그래프를 표시합니다.

# 원형 그래프 생성: 간단한 원형 그래프를 생성합니다.
fig, ax = plt.subplots()
ax.pie([1, 2, 3], labels=['a', 'b', 'c'])  # 데이터와 레이블을 지정하여 원형 그래프를 그립니다.
st.pyplot(fig)  # Streamlit 앱에 그래프를 표시합니다.

# 두 개의 원형 그래프를 나란히 표시: subplots를 사용하여 1행 2열로 원형 그래프를 나란히 배치합니다.
fig, ax = plt.subplots(1, 2)
ax[0].pie([35, 2, 3], labels=['a', 'b', 'c'])  # 첫 번째 원형 그래프
ax[1].pie([1, 2, 3], labels=['a', 'b', 'c'])  # 두 번째 원형 그래프
st.pyplot(fig)  # Streamlit 앱에 그래프를 표시합니다.

# 세 개의 원형 그래프를 나란히 표시: 각 원형 그래프에는 데이터의 비율을 백분율로 표시합니다.
fig, ax = plt.subplots(1, 3)
ax[0].pie([35, 2, 3], labels=['a', 'b', 'c'], autopct='%.2f %%')  # 첫 번째 원형 그래프에 백분율 표시
ax[1].pie([1, 2, 3], labels=['a', 'b', 'c'], autopct='%.2f %%')  # 두 번째 원형 그래프에 백분율 표시
ax[2].pie([1, 34, 3], labels=['a', 'b', 'c'], autopct='%.2f %%')  # 세 번째 원형 그래프에 백분율 표시
st.pyplot(fig)  # Streamlit 앱에 그래프를 표시합니다.

# 이미지 다운로드 버튼: 생성된 마지막 그래프를 이미지로
