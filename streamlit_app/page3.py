import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries."),
        ("user","Question:{question}")
    ]
)



# ollama Gemma LLm 
llm=Ollama(model="nbchat")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

def main():
    #st.set_page_config("Chat PDF")
    st.markdown(
    """
    <h1 style='text-align: center; font-size:24px; '>Neuron Bot</h1>
    """,
    unsafe_allow_html=True)
    st.markdown(
    """
    <h1></h1>
    """,
    unsafe_allow_html=True)

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
    inp = st.text_input("Message",label_visibility='hidden', key=f"input_{st.session_state.input_key}")
    submit = st.button("Send")

    if submit and inp:

        # Get response from the model
        response = chain.invoke({"question":inp})
        
        # Add user query and model response to the chat history
        st.session_state.chat_history.append({"role": "user", "text": inp})
        
        st.session_state.chat_history.append({"role": "bot", "text": response})
        
        st.session_state.input_key += 1
        st.rerun()

        



if __name__ == "__main__":
    main()
