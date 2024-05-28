import streamlit as st

def run():
    # Custom CSS
    st.markdown("""
        <style>
            body {
                background-color: #f0f2f6;
                color: #333;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .header {
                text-align: center;
                padding: 10px 0;
                font-family: 'Arial', sans-serif;
            }
            .header h1 {
                font-size: 48px;
                color: #FFFFFF;
                animation: fadeIn 2s ease-in-out;
            }
            .header p {
                font-size: 20px;
                color: #555;
            }
            .card-row {
                display: flex;
                justify-content: space-around;
                margin-top: 40px;
            }
            .card {
                background-color: #17202A;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                width: 200px;
                text-align: center;
                transition: transform 0.7s ease, background-color 0.7s ease, box-shadow 0.7s ease;
            }
            .card img {
                width: 100%;
                border-radius: 10px 10px 0 0;
                filter: grayscale(0%);
                transition: filter 0.3s ease;
            }
            .card img:hover {
                filter: grayscale(0%);
            }
            .card button {
                background-color: #280332;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
                margin: 20px 0;
                cursor: pointer;
                transition: background-color 0.7s ease;
            }
            .card button:hover {
                background-color: #030C53;
            }
            .card:hover {
                background-color: #2D094D;
                transform: translateY(-20px);
                box-shadow: 0 0 50px #4B1DDA ;
                
            }
            .footer {
                text-align: center;
                padding: 20px 0;
                margin-top: 40px;
                border-top: 1px solid #ddd;
                color: #888;
            }
            @keyframes fadeIn {
                50% { opacity: 0; }
                100% { opacity: 1; }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .custom-h2 {
                font-size: 25px;  /* Change this value to the desired font size */
                color: #FDFEFE;  /* Optional: change the color */
            }
        </style>
    """, unsafe_allow_html=True)

    # HTML structure
    st.markdown("""
        <div class="container">
            <div class="header">
                <h2>Resources</h2>
                <p style="text-align: justify; font-size: 17px;">Welcome to NeuronBit AI, your premier platform for generative AI solutions. Harnessing the power of cutting-edge models like Gemma (2b and 7b), Llama3 (8b and 70b), Gemini-pro, Mixtral with Ollama and Groq. Also Langchain, Pandas AI, Streamlit services, we provide state-of-the-art tools for research and data interaction. Our AI bots enable you to enhance your research by analyzing PDF documents and interacting seamlessly with CSV datasets for insightful analysis and visualization. At NeuronBit AI, we are dedicated to empowering your data-driven decisions with precision and efficiency.
                </p>
            </div>
            <div class="card-row">
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716883584/llama3_yup8a5.png" alt="llama3">
                    <p></p>
                </div>
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716883564/gemini_xup1iy.png" alt="gemini">
                    <p></p>
                </div>
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716883564/gemma_otyp7c.png" alt="gemma">
                    <p></p>
                </div>
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716883564/groq_xsmlym.png" alt="groq">
                    <p></p>
                </div>
            </div>
            <div class="card-row">
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716883580/Ollama_j51msd.png" alt="ollama">
                    <p></p>
                </div>
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716883573/mistral_u07abh.png" alt="mistral">
                    <p></p>
                </div>
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716883576/pandas_s04ew3.png" alt="pandas">
                    <p></p>
                </div>
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716883571/langchain_torc7p.png" alt="langchain">
                    <p></p>
                </div>
            </div>
            <div class="footer">
                <p>&copy; 2024 NeuronBit GenAI. All rights reserved.</p>
            </div>
            
        </div>
    """, unsafe_allow_html=True)




