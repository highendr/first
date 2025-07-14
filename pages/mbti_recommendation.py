
import streamlit as st

st.title("MBTI 기반 직업 추천")

mbti = st.selectbox("당신의 MBTI는?", ["INTJ", "ENFP", "ISTJ", "ESFP"])

recommendations = {
    "INTJ": ["데이터 과학자", "시스템 설계자"],
    "ENFP": ["마케터", "스타트업 창업자"],
    "ISTJ": ["회계사", "공무원"],
    "ESFP": ["방송인", "이벤트 플래너"]
}

if mbti:
    st.write("추천 직업:")
    for job in recommendations.get(mbti, []):
        st.markdown(f"- {job}")

