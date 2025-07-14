import streamlit as st
import pandas as pd

st.title("지도 시각화 웹앱")

uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
print(uploaded_file)
print("after upload")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.map(df)
else:
    data = {
        'latitude': [37.5665, 37.5651, 37.5673],
        'longitude': [126.9780, 126.9768, 126.9821]
    }
    df = pd.DataFrame(data)
    st.write("샘플 데이터로 지도 표시 중입니다.")
    st.map(df)
