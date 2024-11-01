import streamlit as st

# 꼭 pages폴더 안에 만들어야 페이지 라우팅이 됨 (streamlit이 pages폴더를 찾음)
# 페이지는 사이드바에 
# 순서를 변경하고 싶다면 파일 이름앞에 숫자를 써주면됨 ex) 01_DocumentGPT.py 아니면 1_DocumentGPT.py 이렇게 앞에 숫자만 적어주면 됨 (그럼 상위 파일로 올라오니까)
st.title("DocumentGPT")

with st.sidebar:
    st.title("DocumentGPT 사이드바")
    st.write("DocumentGPT 사이드바 내용")