
import streamlit as st

st.title("BMI 계산기")

height = st.number_input("키(cm)", min_value=100, max_value=250)
weight = st.number_input("몸무게(kg)", min_value=30, max_value=200)

if st.button("BMI 계산"):
    bmi = weight / ((height / 100) ** 2)
    st.write(f"BMI는 {bmi:.2f}입니다.")
