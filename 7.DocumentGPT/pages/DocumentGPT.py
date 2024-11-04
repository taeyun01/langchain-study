import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, CacheBackedEmbeddings
from langchain.vectorstores import FAISS
from langchain.storage import LocalFileStore
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough

st.set_page_config(page_title="DocumentGPT", page_icon="📝")

st.title("DocumentGPT")

st.markdown("""
파일을 업로드하고 대화를 나누어보세요!
""")

# 업로드한 파일을 임베딩하는 함수
@st.cache_data(show_spinner="업로드 중...")
def embed_file(file):
    file_content = file.read() # 업로드된 파일의 내용을 읽어옴
    file_path = f"./7.DocumentGPT/.cache/files/{file.name}" # 파일을 캐시 디렉토리에 저장할 경로 설정 
    with open(file_path, "wb") as f: # 파일을 캐시 디렉토리에 바이너리 모드로 저장
        f.write(file_content)
    cache_dir = LocalFileStore(f"./7.DocumentGPT/.cache/embeddings/{file.name}") # 임베딩을 캐시할 디렉토리 설정
    # 텍스트 분할기 설정 - 문서를 청크 단위로 분할
    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n", # 문자열을 분할하는 기준
        chunk_size=600,  # 각 청크의 최대 크기
        chunk_overlap=100,  # 청크 간 중복되는 문자 수
    )
    loader = UnstructuredFileLoader(file_path) # 파일 로더를 사용하여 문서 로드
    docs = loader.load_and_split(text_splitter=splitter) # 문서를 청크 단위로 분할
    embeddings = OpenAIEmbeddings() # OpenAI 임베딩 모델 초기화
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir) # 임베딩을 캐시하여 재사용할 수 있도록 설정
    vectorstore = FAISS.from_documents(docs, cached_embeddings) # 분할된 문서를 벡터 저장소에 저장
    retriever = vectorstore.as_retriever() # 벡터 저장소를 검색 가능한 형태로 변환
    return retriever # 검색 가능한 형태로 변환된 벡터 저장소 반환

# 채팅 메시지를 화면에 표시하고 저장하는 함수
def send_message(message, role, save=True):
    # streamlit의 chat_message 컴포넌트를 사용하여 메시지 표시
    with st.chat_message(role):
        st.markdown(message)
    # save가 True인 경우 메시지를 세션 상태에 저장
    if save:
        st.session_state["messages"].append({"message": message, "role": role}) 

# 이전 대화 내역을 화면에 다시 표시하는 함수
def paint_history():
    # 세션에 저장된 모든 메시지를 순회하며 표시
    for message in st.session_state["messages"]:
        send_message(
            message["message"],
            message["role"],
            save=False,  # 이미 저장된 메시지이므로 다시 저장하지 않음
        )

# 사이드바에 파일 업로더 배치
with st.sidebar:
    file = st.file_uploader(".txt .pdf .docx 파일을 업로드 해주세요.", type=["txt", "pdf", "docx"])

# 파일이 업로드된 경우
if file:
    retriever = embed_file(file) # 파일을 임베딩하여 검색 가능한 형태로 변환
    send_message("대답할 준비가 되었습니다!", "AI", save=False)
    paint_history() # 이전 대화 내역 표시
    message = st.chat_input("질문을 입력하세요.") # 사용자 입력 받기
    if message:
        send_message(message, "user") # 사용자 메시지 표시 및 저장
        send_message("테스트~~~~", "ai")
# 파일이 업로드되지 않은 경우
else:
    st.session_state["messages"] = [] # 대화 내역 초기화
