import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from index import css, bot_template, user_template

# 读取PDF的内容
def getText(document):
    text = ""
    for pdf in document:
        read = PdfReader(pdf)
        for page in read.pages:
            text += page.extract_text()
    return text

# 分化读取到的PDF的内容
def splitText(text):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    parts = splitter.split_text(text)
    return parts

# langchain vector表示这些分化部分（embeddings）
def vectorRepresent(parts):
    embeddings = OpenAIEmbeddings()
    vector = FAISS.from_texts(texts=parts, embedding=embeddings)
    return vector

# 对话
def conversation(vector):
    llm = ChatOpenAI()

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector.as_retriever(),
        memory=memory
    )
    return chain

# 分析用户提的问题
def userInput(question):
    response = st.session_state.conversation({'question': question})
    st.session_state.chat_history = response['chat_history']

    for i, msg in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", msg.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", msg.content), unsafe_allow_html=True)

# 主程序
def main():
    load_dotenv()
    st.set_page_config(page_title="训练问答测试",
                       page_icon="📃")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("智能客服")
    question = st.text_input("请提问")
    if question:
        userInput(question)

    with st.sidebar:
        st.subheader("文件")
        pdf_docs = st.file_uploader(
            "上传PDF文件", accept_multiple_files=True)
        if st.button("上传"):
            with st.spinner("上传中"):
                # 读PDF内容
                text = getText(pdf_docs)
                # 分化内容
                textParts = splitText(text)
                # 用vector表示分化
                vector = vectorRepresent(textParts)
                # 生成对话
                st.session_state.conversation = conversation(vector)

if __name__ == '__main__':
    main()
