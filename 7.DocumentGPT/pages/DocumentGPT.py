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
    st.session_state["messages"] = [] # session_state에 messages key값을 추가 -> ({"messages":[]})

# st.write(st.session_state)

# svae를 True로 설정하면 user나 AI가 처음 메세지를 보낼 때 sand_message함수가 실행되고 메세지를 cache안에 저장함
def sand_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
    if save:
        st.session_state.messages.append({"message": message ,"role": role}) # session_state messages리스트에 user메세지와 AI메세지를 append하고 있음

# st.session_state.messages에 있는 모든 메시지를 출력 (sand_message함수에 매개변수로 보내주어 메세지 ui출력)
for message in st.session_state["messages"]:
    sand_message(message["message"],
                 message["role"],
                 save=False) # 메세지를 session_state에 중복해서 저장하지 않기위해 save=False로 설정 (사용자가 메세지를 보낼때마다 실행되는데 중복해서 저장하면 메세지가 중복됨)
                            # 우리가 메세지를 보내면 메세지를 계속 다시 그림 (DataFlow로 인해 코드 다시 실행)
                            
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
