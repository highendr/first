import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path)

plt.title('제목', fontproperties=fontprop)

st.title("기본 선그래프")

df = pd.read_csv("sample1.csv", encoding="euc-kr")
st.dataframe(df.reset_index(drop=True))

fig, ax = plt.subplots()
df.plot(x='년도', y='인구수', kind='line', ax=ax)
plt.title('년도별 인구 변화')
st.pyplot(fig)
