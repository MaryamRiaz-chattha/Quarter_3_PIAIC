import streamlit as st
from PyPDF2 import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# ✅ Page config sabse pehle honi chahiye
st.set_page_config(page_title="AI PDF Reader", page_icon="📄", layout="wide")

# 🎨 Inline CSS (no external file needed)
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    font-family: 'Inter', sans-serif;
    color: #f1f5f9;
}

/* Container for better layout */
.main {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Title */
h1.neon-text {
    font-size: 2.4rem;
    font-weight: 700;
    color: #facc15; /* Yellow */
    text-align: center;
    margin-bottom: 0.5rem;
}

/* Subtitle */
p.subtitle {
    text-align: center;
    font-size: 1rem;
    color: #cbd5e1;
    margin-bottom: 2rem;
}

/* Upload Section */
.upload-section {
    border: 2px dashed #facc15;
    border-radius: 12px;
    padding: 30px;
    background: rgba(255, 255, 255, 0.05);
    text-align: center;
    transition: all 0.3s ease;
}
.upload-section:hover {
    background: rgba(255, 255, 255, 0.08);
    transform: scale(1.02);
    border-color: #fde047;
}

/* Input */
input[type="text"] {
    width: 100%;
    padding: 12px;
    margin-top: 15px;
    border-radius: 8px;
    border: 2px solid #facc15;
    background: rgba(0, 0, 0, 0.3);
    color: #f1f5f9;
    font-size: 16px;
    outline: none;
}

/* Button */
button {
    background: #facc15;
    color: #0f172a;
    padding: 12px 20px;
    border-radius: 8px;
    border: none;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    margin-top: 20px;
    transition: all 0.3s ease;
}
button:hover {
    background: #fde047;
    box-shadow: 0px 4px 12px rgba(250, 204, 21, 0.4);
    transform: translateY(-2px);
}

/* AI Response Box */
.response-box {
    margin-top: 25px;
    padding: 20px;
    border: 2px solid #facc15;
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.05);
    font-size: 1.1rem;
}
</style>
""", unsafe_allow_html=True)

# 🤖 Gemini AI model initialize karna
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=os.getenv("GEMINI_API_KEY"))

# 🏷️ Page Title
st.markdown("<h1 class='neon-text'>📄 AI PDF Reader</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Upload your PDF and ask questions related to it.</p>", unsafe_allow_html=True)

# 📂 PDF Upload Section
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)
    document = ""
    for page in pdf_reader.pages:
        document += page.extract_text()

    user_input = st.text_input("Enter your question:")
    
    if st.button("Ask AI"):
        instruction = f"""
        You have to guide the user according to the provided document.
        - The user input is here: {user_input}
        - The document is here: {document}
        If the user asks something outside the document, you must say you cannot answer that question.
        """
        response = llm.invoke(instruction)
        st.markdown('<div class="response-box">', unsafe_allow_html=True)
        st.write("### AI Response:")
        st.write(response.content)
        st.markdown('</div>', unsafe_allow_html=True)
