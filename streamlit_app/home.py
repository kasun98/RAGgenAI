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
                padding: 50px 0;
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
                background-color: #450954;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                width: 300px;
                text-align: center;
                transition: transform 0.7s ease, background-color 0.7s ease, box-shadow 0.7s ease;
            }
            .card img {
                width: 100%;
                border-radius: 10px 10px 0 0;
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
                <h1>NeuronBit AI</h1>
                <p>Enhance your research, interact with data, and explore AI capabilities with NeuronBit GenAI.</p>
            </div>
            <div class="card-row">
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716803149/ra_skuvpd.jpg" alt="Researcher">
                    <p>
                        <p style="font-size: 23px; font-weight: bold;">Research AI<p/>
                        <p style="text-align: justify; color: #ABB2B9; padding: 15px;">Enhance your research with our Research AI Bot. Simply upload your documents in PDF format. You can then ask questions, and the AI bot will provide accurate answers based on the content of your uploaded documents.</p>
                    </p>
                </div>
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716803144/data_wyaiqa.jpg" alt="Chat with Data">
                    <p>
                        <p style="font-size: 23px; font-weight: bold;">Data AI</p>
                        <p style="text-align: justify; color: #ABB2B9; padding: 15px;">Interact with your datasets using our Data AI Bot. Upload your CSV files and ask any questions related to your dataset. The AI bot will answer your queries and can also visualize the data for better insights.</p>
                    </p>
                </div>
                <div class="card">
                    <img src="https://res.cloudinary.com/djw3z53pj/image/upload/v1716803146/gen_piodih.jpg" alt="General Bot">
                    <p>
                        <p style="font-size: 23px; font-weight: bold;">Chat Bot</p>
                        <p style="text-align: justify; color: #ABB2B9; padding: 15px;">Meet our friendly AI Chat Bot, designed for engaging and intelligent conversations. Whether you need assistance, have queries, or just want to chat, this bot is here to provide you with a seamless conversational experience.</p>
                    </p>
                </div>
            </div>
            <div class="footer">
                <p>&copy; 2024 NeuronBit GenAI. All rights reserved.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)


