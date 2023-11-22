import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd


st.title("데이터 시각화:plt")

x = range(20) # 0, 1, .. 19
y = [value**2 for value in x]+np.random.rand(20)*100
y1 = [value for value in x]+np.random.rand(20)*100
y2 = [value**3 for value in x]+np.random.rand(20)*100


fig, ax = plt.subplots()
ax.plot(x, y)# 꺾은선그래프


fig, ax = plt.subplots(1, 2)
plt.figure(figsize = (4,4))
ax[0].plot(x, y1)
ax[1].plot(x, y2)# 꺾은선그래프
st.pyplot(fig)
plt.scatter(x, y) #산점도
plt.show()

plt.bar(x, y) #막대그래프
plt.show()


fig, ax = plt.subplots(1, 3)
ax[0].pie([35, 2, 3], labels=['a', 'b', 'c'], autopct='%.2f %%')  # 첫 번째 원형 그래프에 백분율 표시
ax[1].pie([1, 2, 3], labels=['a', 'b', 'c'], autopct='%.2f %%')  # 두 번째 원형 그래프에 백분율 표시
ax[2].pie([1, 34, 3], labels=['a', 'b', 'c'], autopct='%.2f %%')  # 세 번째 원형 그래프에 백분율 표시
st.pyplot(fig)  # Streamlit 앱에 그래프를 표시합니다.
