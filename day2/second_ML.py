import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

st.title("Machine Learning in Streamlit")
# 데이터셋 로드
@st.cache_data  # 데이터 캐싱
def load_data():
    # data from https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data?select=train.csv
    data = pd.read_csv(".streamlit/train.csv")  # 실제 파일 경로로 변경해야 합니다.
    # data = pd.read_csv("https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data?select=train.csv")
    return data

df = load_data()
st.write(df.head())
# st.table(df)
# st.dataframe(df)

# 간단한 데이터 전처리
# 필요한 특성을 선택하고 결측치를 처리하는 과정을 추가하세요.
# 예를 들어, 아래 코드는 'LotArea', 'OverallQual', 'OverallCond', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd' 특성만 사용하고 결측치를 중간값으로 채웁니다.
features = ['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'YearBuilt', 'FullBath']
df[features] = df[features].fillna(df[features].median())

# 모델 훈련
X = df[features]
y = df['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(X_train, y_train)

# 모델 성능 평가
st.subheader("모델 성능")
st.write("Mean Absolute Error: ", mean_absolute_error(y_test, model.predict(X_test)))

# 사용자 입력 받기
st.subheader("가격 예측을 위한 파라미터 입력")

def user_input_features():
    input_data = {}
    for feature in features:
        input_data[feature] = st.number_input(f"Enter {feature}", value=float(df[feature].median()))
    return pd.DataFrame(input_data, index=[0])

input_df = user_input_features()
import numpy as np

# 예측 버튼
if st.button('Predict'):
    # 입력 데이터에 대한 예측
    prediction = model.predict(input_df)
    
    st.write(f'## Predicted Sale Price : ${int(prediction[0])}')
    st.write(f"## 한화 {np.round(prediction[0]*(1/0.00076)/100000000, 3)}억!")
    st.balloons()

