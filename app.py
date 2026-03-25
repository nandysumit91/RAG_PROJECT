import streamlit as st
import pdfplumber
import google.generativeai as genai

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# -------------------------------
# 🔑 SET YOUR GEMINI API KEY HERE
# -------------------------------
genai.configure(api_key="AIzaSyAew3WSN3AkRz0HKy1vm6mBmAOS_E3niHE")

# -------------------------------
# 1. Extract text from PDF
# -------------------------------
def load_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

# -------------------------------
# 2. Split text into chunks
# -------------------------------
def split_text(text):
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_text(text)

# -------------------------------
# 3. Create vector store
# -------------------------------
def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    db = FAISS.from_texts(chunks, embeddings)
    return db

# -------------------------------
# 4. Ask question (Gemini)
# -------------------------------
DEFAULT_GEMINI_MODEL = "gemini-2.5-flash"  # stable model name for v1beta


def ask_question(db, query):
    docs = db.similarity_search(query, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    try:
        model = genai.GenerativeModel(DEFAULT_GEMINI_MODEL)
    except Exception as e:
        st.error(f"Gemini model not available: {e}")
        raise

    prompt = f"""
    You are a helpful assistant.

    Answer ONLY from the given context.
    If answer is not present, say: Not found in document.

    Context:
    {context}

    Question:
    {query}
    """

    try:
        response = model.generate_content(prompt)
    except Exception as e:
        st.error(f"Gemini API request failed: {e}")
        raise

    return response.text

# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="PDF Q&A System")

st.title("📄 PDF Q&A System (Gemini Powered 🚀)")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with st.spinner("Processing PDF..."):
        text = load_pdf(uploaded_file)

        if not text:
            st.error("No text found in PDF ❌")
        else:
            chunks = split_text(text)
            db = create_vectorstore(chunks)

            st.success("PDF processed successfully ✅")

            query = st.text_input("Ask a question:")

            if query:
                with st.spinner("Thinking..."):
                    answer = ask_question(db, query)

                    st.write("### Answer:")
                    st.write(answer)