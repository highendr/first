import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.title("기본 선그래프")

# CSV 파일 읽기
df = pd.read_csv("sample1.csv", encoding="euc-kr")

# 인덱스 없이 표 출력
st.dataframe(df.reset_index(drop=True))

# 선그래프 출력
fig, ax = plt.subplots()
df.plot(x='년도', y='인구수', kind='line', ax=ax)
plt.title('년도별 인구 변화')
st.pyplot(fig)
