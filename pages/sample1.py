import streamlit as st
import pandas as pd

# 타이틀
st.title("📊 년도별 인구 변화 시각화")

# CSV 데이터 불러오기 (EUC-KR 인코딩)
df = pd.read_csv("sample1.csv", encoding='euc-kr')

# 원본 데이터 출력 (왼쪽 인덱스 숨기기)
st.subheader("📂 원본 데이터")
st.dataframe(df.style.hide(axis="index"))

# 라인 차트 그리기 (년도 x축, 인구수 y축)
st.subheader("📈 년도별 인구 변화 라인 차트")
chart_data = df.set_index('년도')['인구수']
st.line_chart(chart_data)
