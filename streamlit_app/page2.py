import streamlit as st 
from langchain_community.llms import Ollama 
import pandas as pd
from pandasai import SmartDataframe
import os
from langchain_groq import ChatGroq
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
groq_api_key=os.getenv('GROQ_API_KEY')

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

def main():
    
    st.markdown(
    """
    <h1 style='text-align: center; font-size:24px; '>Chat with Your Data</h1>
    """,
    unsafe_allow_html=True)

    model_options = ["Gemini-pro", "Gemma-2b", "Gemma-7b-groq", "Mixtral-8x7b-groq", "Llama3-8b-groq", "Llama3-70b-groq"]
    selected_model = st.selectbox("Select a LLM Model", model_options)
    s_model = get_model(selected_model)

    uploader_file = st.file_uploader("Upload a CSV file to start", type= ["csv"])

    
    

    if uploader_file is not None:
        data = pd.read_csv(uploader_file)
        st.write(data.head(5))
        df = SmartDataframe(data, config={"llm": s_model})
        prompt = st.text_area("Enter your prompt:")

        if st.button("Generate"):
            if prompt:
                with st.spinner("Generating response..."):
                    st.write(df.chat(prompt))
            else:
                st.warning("Please enter a prompt!")



    
    

if __name__ == "__main__":
    main()