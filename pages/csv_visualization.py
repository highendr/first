
import streamlit as st
import pandas as pd

st.title("데이터 시각화")

df = pd.read_csv("sample_data.csv",encoding="euc-kr" )
st.dataframe(df)
st.line_chart(df.set_index(df.columns[0]))
