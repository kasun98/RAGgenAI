import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from PyPDF2 import PdfReader
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
groq_api_key=os.getenv('GROQ_API_KEY')

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_model(selected_model):
    model_options = ["Gemini-pro", "Gemma-2b", "Gemma-7b-groq", "Mixtral-8x7b-groq", "Llama3-8b-groq", "Llama3-70b-groq"]
    if selected_model==model_options[0]:
        s_model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
    if selected_model==model_options[1]:
        s_model = Ollama(model="gemma:2b", temperature=0.5)
    if selected_model==model_options[2]:
        s_model = ChatGroq(groq_api_key=groq_api_key, model_name="gemma-7b-it")
    if selected_model==model_options[3]:
        s_model = ChatGroq(groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")    
    if selected_model==model_options[4]:
        s_model = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-8b-8192")
    if selected_model==model_options[5]:
        s_model = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-70b-8192")
    return s_model

def get_conversational_chain(s_model):

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = s_model

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(user_question,s_model):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain(s_model)

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)
    
    #st.write("Reply: ", response["output_text"])
    return response["output_text"]
    




def main():
    #st.set_page_config("Chat PDF")
    st.markdown(
    """
    <h1 style='text-align: center; font-size:24px; '>Chat with Your Documents</h1>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <h1></h1>
    """,
    unsafe_allow_html=True)

    model_options = ["Gemini-pro", "Gemma-2b", "Gemma-7b-groq", "Mixtral-8x7b-groq", "Llama3-8b-groq", "Llama3-70b-groq"]
    selected_model = st.selectbox("Select a LLM Model", model_options)

    s_model = get_model(selected_model)

    pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit Button", accept_multiple_files=True)
    
    if st.button("Submit"):
        with st.spinner("Processing..."):
            raw_text = get_pdf_text(pdf_docs)
            text_chunks = get_text_chunks(raw_text)
            get_vector_store(text_chunks)
            st.success("Done")

    
        

    # Initialize session state for chat history if not already done
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    if 'input_key' not in st.session_state:
        st.session_state.input_key = 0

    # Define CSS for chat interface
    chat_css = """
    <style>
    .chat-box {
        max-width: auto;
        margin: auto;
        padding: 10px;
        border-radius: 15px;
        background-color: rgba(255,255,255,0);
        transition: background-color 1s ease, color 1s ease;
        overflow-y: auto;
        height: 400px;
        border: 0px solid #ccc;
    }

   

    .message-container {
            display: flex;
            justify-content: flex-end;
            margin: 5px 0;
        }

    .message {
        display: inline-block;
        padding: 10px;
        border-radius: 15px;
        transition: background-color 1s ease, color 1s ease;
    }

    .user-message {
        background-color: #1E8449;
        text-align: right;
        border-radius: 15px 0 15px 15px;
        color: white;
    }

    .user-message:hover {
        background-color: #138D75; 
        color: white;
    }

    .bot-message {
        background-color: #343435 ;
        text-align: left;
        border-radius: 0 15px 15px 15px;
        color: white;
    }

    .bot-message:hover {
        background-color: #2C3E50; 
        color: white;
    }

    .user-container {
        justify-content: flex-end;
    }

    .bot-container {
        justify-content: flex-start;
    }

    </style>
    """

    # Display chat interface
    st.markdown(chat_css, unsafe_allow_html=True)


    # Display the chat history
    chat_history_str = '<div class="chat-box" style="max-height: 400px; overflow-y: auto;">'
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            chat_history_str += f'<div class="message-container user-container" style="margin-bottom: 10px;"><span class="message user-message"> {message["text"]}</span></div>'
        else:
            chat_history_str += f'<div class="message-container bot-container" style="margin-bottom: 10px;"><span class="message bot-message"> {message["text"]}</span></div>'
    chat_history_str += '</div>'
    st.markdown(chat_history_str, unsafe_allow_html=True)

    # Text input for user query
    inp = st.text_input("Message", key=f"input_{st.session_state.input_key}")
    submit = st.button("Send")

    if submit and inp:
        # Get response from the model
        response = user_input(inp, s_model)
        
        # Add user query and model response to the chat history
        st.session_state.chat_history.append({"role": "user", "text": inp})
        
        st.session_state.chat_history.append({"role": "bot", "text": response})
        
        st.session_state.input_key += 1
        st.rerun()



    
    



if __name__ == "__main__":
    main()
