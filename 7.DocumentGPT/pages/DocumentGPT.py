import streamlit as st
import time

st.set_page_config(page_title="DocumentGPT", page_icon="📝")

# 꼭 pages폴더 안에 만들어야 페이지 라우팅이 됨 (streamlit이 pages폴더를 찾음)
st.title("DocumentGPT")

# 메세지를 리스트에 저장해도 DataFlow로 인해 새로고침되어 다시 초기화됨.
# messages = []

# session_state를 사용하면 데이터를 보존할 수 있음. 메시지를 계속 이어서 작성할 수 있다는 의미. 하지만 새로고침시 사라짐(session_state는 object임)
# 만약 st.session_state가 massages라는 key값이 없으면 빈 리스트로 initialize함
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# st.write(st.session_state.messages)

def sand_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
    if save:
        st.session_state.messages.append({"message": message ,"role": role})

for message in st.session_state["messages"]:
    sand_message(message["message"], message["role"], save=False)


with st.sidebar:
    st.header("DocumentGPT 대화내용")

message = st.chat_input("메세지를 입력해주세요.")

if message:
    sand_message(f"유저임 : {message}", "user")
    time.sleep(1)
    sand_message(f"로봇임 : {message}", "AI")

    with st.sidebar:
        for message in st.session_state.messages:
            st.write(message["message"])
