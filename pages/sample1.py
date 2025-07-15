import streamlit as st
import pandas as pd

# 타이틀
st.title("📊 년도별 인구 변화 시각화")

# CSV 데이터 불러오기 (EUC-KR 인코딩)
df = pd.read_csv("sample1.csv", encoding='euc-kr')

# 첫 번째 열 삭제
df = df.drop(df.columns[0], axis=1)

# 원본 데이터 출력 (인덱스 숨기기)
st.subheader("📂 원본 데이터")
st.dataframe(df.style.hide(axis="index"))

# 2020~2024년 데이터만 추출
df = df[df['년도'].isin([2020, 2021, 2022, 2023, 2024])]

# 라인 차트 그리기
st.subheader("📈 2020년부터 2024년까지 인구 변화 라인 차트")
st.line_chart(df.set_index('년도')['인구수'])
