import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 폰트 자동 설정 (한글 폰트 있으면 사용)
font_list = [f.name for f in fm.fontManager.ttflist if 'Gothic' in f.name or 'Nanum' in f.name]
if font_list:
    plt.rcParams['font.family'] = font_list[0]
else:
    plt.rcParams['font.family'] = 'sans-serif'

plt.rcParams['axes.unicode_minus'] = False

st.title("기본 선그래프")

df = pd.read_csv("sample1.csv", encoding="euc-kr")
st.dataframe(df.reset_index(drop=True))

fig, ax = plt.subplots()
df.plot(x='년도', y='인구수', kind='line', ax=ax)
plt.title('년도별 인구 변화')
st.pyplot(fig)
