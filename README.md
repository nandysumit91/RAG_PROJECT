# 📄 PDF Q&A System (RAG with Gemini)

An AI-powered Question Answering system that allows users to upload a PDF and ask questions.
The system retrieves relevant content using vector search and generates accurate answers using Google Gemini.

---

## 🚀 Features

* 📄 Upload PDF files
* ✂️ Automatic text extraction & chunking
* 🔍 Semantic search using FAISS
* 🤖 Accurate answers using Gemini API
* ⚡ Fast and interactive UI with Streamlit

---

## 🧠 How It Works

1. PDF is uploaded
2. Text is extracted using `pdfplumber`
3. Text is split into chunks
4. Chunks are converted into embeddings
5. Stored in FAISS vector database
6. User query → similarity search
7. Context sent to Gemini → final answer

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* HuggingFace Embeddings
* Google Gemini API

---

## 📦 Installation

```bash
pip install streamlit pdfplumber langchain-text-splitters langchain-community sentence-transformers faiss-cpu google-generativeai
```

---

## 🔑 Setup API Key

Replace in `app.py`:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📸 Demo

Upload a PDF and ask questions like:

* What is the main topic?
* What is the name of the person?
* Summarize the document

---

## 📁 Project Structure

```
rag-project/
│── app.py
│── requirements.txt
│── README.md
│── data/
```

---

## 🎯 Example Output

**Question:** What is the main topic?
**Answer:** The document is a resume describing skills, projects, and experience.

---

## 🔥 Future Improvements

* 📑 Multi-PDF support
* 📌 Source citation (show page number)
* 🌐 Web deployment
* 💬 Chat history

---

## 👨‍💻 Author

**Sumit Kumar Nandy**

* GitHub
* LinkedIn
* Portfolio

---

## ⭐ Contribute

Feel free to fork this project and improve it!
