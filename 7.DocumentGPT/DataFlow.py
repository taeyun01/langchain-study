import streamlit as st
from langchain.prompts import ChatPromptTemplate
from datetime import datetime

# 로컬 실행: streamlit run ./7.DocumentGPT/DataFlow.py
today = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")

st.title("Streamlit Data Flow")

st.subheader("Welcome to Streamlit")

st.write(today)

model = st.selectbox("AI 모델 선택", (
    "GPT-4o",
    "GPT-4o-mini",
    "Gemini 1.5 Pro",
))

st.write("내가 선택한 모델 : ", model)

st.markdown("""
            #### Streamlit의 Data flow와 data가 처리되는 방식에 대해 알아보자
            - 결론부터 말하면 data가 변경될 때마다 python 파일 전체가 다시 실행된다.
            - 사용자가 무언갈 입력하거나, 아니면 selectbox를 변경해서 data가 변경될 때마다 python 파일 전체가 위부터 아래까지 전부 다시 실행된다.
            - selectbox를 변경해보고 위 시간이 변경되는지 확인해보자.
            - 리액트 같이 바뀐 부분만 렌더링 되는 것이 아니라 전체가 다시 실행된다.
""")

st.markdown(""" --- """)
st.write(today)


name = st.text_input("이름을 입력해주세요.", value="이름 입력해라")

st.write("이름 : ", name)

st.markdown("""
            - 이처럼 모든 데이터가 변경될 때마다 전체가 다시 실행된다.
            - 이게 Streamlit의 Data flow다. (새로고침 같은게 아닌 파일 코드가 다시 실행 되는 것)
            - 그래도 Streamlit에는 cache를 제공하는 매커니즘이 있어서 어떤건 다시 실행 되지 않는다. 챗봇 구현할 때 유용하다. 나중에 알아보자
""")

st.markdown(""" --- """)
st.write(today)

value = st.slider("값을 선택해주세요.", min_value=0.1, max_value=1.0)

st.write("선택한 값 : ", value)

st.markdown("""
            - 위 슬라이드 바를 움직여보자. 값이 변경 될 때 마다 모든 코드가 다시 실행된다. (시간 확인)
            - 그래서 if문 조건에 따라 위젯을 보여주거나 숨기거나 할 때 코드가 다시 실행되면서 참이면 보여주고 거짓이면 숨기는 것이 가능하다.
            """)

boolean = st.selectbox("참 거짓", (
    "참",
    "거짓",
))

if boolean == "참":
    st.write("참이면 보여준다.")
else:
    st.write("거짓이면 숨긴다.")
