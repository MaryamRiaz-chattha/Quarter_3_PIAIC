import streamlit as st
from PyPDF2 import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# ✅ Page config sabse pehle honi chahiye
st.set_page_config(page_title="AI PDF Reader", page_icon="📄", layout="wide")

# 🎨 CSS File ko Inject karna
with open("styles.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🤖 Gemini AI model initialize karna
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=os.getenv("GEMINI_API_KEY"))

# 🏷️ Page Title
st.markdown('<div class="background-image">', unsafe_allow_html=True)
st.markdown("<h1 class='neon-text'>📄 AI PDF Reader</h1>", unsafe_allow_html=True)
st.write("Upload your PDF and ask questions related to it.")
st.markdown('</div>', unsafe_allow_html=True)

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
        st.write("### AI Response:")
        st.write(response.content)
