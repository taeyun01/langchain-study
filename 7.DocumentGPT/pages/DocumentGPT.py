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

def embed_file(file):
    # st.write(file)
    file_content = file.read()
    file_path = f"./7.DocumentGPT/.cache/files/{file.name}" # 파일을 미리 생성해줘야함
    # st.write(file_content)
    # st.write(file_path)
    with open(file_path, "wb") as f: # file이름이 위에 존재해 f로 변경
        f.write(file_content) # file_content를 전부 쓸 거임
    cache_dir = LocalFileStore(f"./.cache/embeddings/{file.name}") # 해당 디렉토리에서 임베딩을 찾음
    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n",
        chunk_size=600,
        chunk_overlap=100,
    )
    loader = UnstructuredFileLoader(file_path)
    docs = loader.load_and_split(text_splitter=splitter)
    embeddings = OpenAIEmbeddings()
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)
    vectorstore = FAISS.from_documents(docs, cached_embeddings)
    retriever = vectorstore.as_retriever()
    # docs = retriever.invoke("파일 내용을 설명해주세요.")
    # st.write(docs)
    return retriever

file = st.file_uploader(".txt .pdf .docx 파일을 업로드 해주세요.", type=["txt", "pdf", "docx"])

if file:
    retriever = embed_file(file)
    s = retriever.invoke("파일 내용을 설명해주세요.")
    st.write(s)