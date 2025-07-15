import streamlit as st
import pandas as pd

# 타이틀
st.title("📊 년도별 인구 변화 시각화")

# CSV 데이터 불러오기 (EUC-KR 인코딩)
df = pd.read_csv("sample1.csv", encoding='euc-kr')

# 원본 데이터 출력 (인덱스 숨기기)
st.subheader("📂 원본 데이터")
st.dataframe(df.style.hide(axis="index"))

# x축을 2020~2024년으로 강제 설정
df = df[df['년도'].isin([2020, 2021, 2022, 2023, 2024])]

# 라인 차트용 데이터 구성 (인덱스 없이 바로 그리기)
st.subheader("📈 2020년부터 2024년까지 인구 변화 라인 차트")
st.line_chart(df.set_index('년도')['인구수'])

