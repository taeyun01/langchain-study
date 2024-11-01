import streamlit as st

# 페이지 타이틀, 파비콘 설정
st.set_page_config(page_title="DocumentGPT", page_icon="📝")

# 로컬 실행: streamlit run ./7.DocumentGPT/DataFlow.py
st.title("DocumentGPT")


# with st.sidebar: 블록안에 있는 모든 코드는 st.sidebar를 쓰지 않고 st만 써도 사이드바에 표시됨
with st.sidebar:
    st.title("Sidebar Title") # st.sidebar.title()과 동일
    st.text_input("사이드바 입력")
    

# 다른 위젯들도 이런식으로 사용하면 편함
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.title("Tab 1")
    st.write("Tab 1 내용")

with tab2:
    st.title("Tab 2")

with tab3:
    st.title("Tab 3")
