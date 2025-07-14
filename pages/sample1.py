import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("난이도 하 - 기본 선그래프")

df = pd.read_csv("sample1.csv",encoding="euc-kr")
st.dataframe(df)

fig, ax = plt.subplots()
df.plot(x='년도', y='인구수', kind='line', ax=ax)
plt.title('년도별 인구 변화')
st.pyplot(fig)
