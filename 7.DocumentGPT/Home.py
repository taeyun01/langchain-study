import streamlit as st

# 페이지 타이틀, 파비콘 설정
st.set_page_config(page_title="DocumentGPT", page_icon="🤖")

# 로컬 실행: streamlit run ./7.DocumentGPT/DataFlow.py
st.title("DocumentGPT")

st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/DocumentGPT.py", label="DocumentGPT", icon="📝")
st.page_link("pages/PrivateGPT.py", label="PrivateGPT", icon="🔐")
st.page_link("pages/QuizGPT.py", label="QuizGPT", icon="🧠")
