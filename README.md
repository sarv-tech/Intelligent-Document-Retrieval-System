# 🤖 NoteBot AI

### Intelligent Document Retrieval System using RAG

*Upload notes. Ask questions. Learn smarter with AI.* 🚀

---

## 🌌 Overview

NoteBot AI is an AI-powered Retrieval-Augmented Generation (RAG) application that transforms static PDF documents into an intelligent learning assistant.

Built using modern Generative AI technologies, the platform allows users to upload multiple PDFs and ask context-aware questions directly from their notes using semantic search and Large Language Models (LLMs).

The system combines vector embeddings, semantic retrieval, and Groq-powered LLM responses to deliver fast, accurate, and educational answers.

---

# 🚀 Live Demo

🔗 https://intelligent-document-retrieval-system-vhgunrmheo8rycaxupxsbb.streamlit.app/

---

# 🌟 Key Features

## 📚 Document Intelligence

* Upload multiple PDF documents
* Automatic text extraction from PDFs
* Smart chunking for efficient retrieval
* Semantic search powered by vector embeddings

## 🤖 AI-Powered Question Answering

* Retrieval-Augmented Generation (RAG)
* Context-aware responses
* Groq Llama 3.1 integration
* Beginner-friendly AI tutor responses
* Fast inference with low latency

## ⚡ Interactive Experience

* Streamlit-based responsive UI
* Real-time AI answers
* Expandable chunk visualization
* Clean and minimal interface

---

# 🛠️ Tech Stack

| Layer           | Technologies                      |
| --------------- | --------------------------------- |
| Frontend        | Streamlit                         |
| AI Framework    | LangChain                         |
| Embeddings      | HuggingFace Sentence Transformers |
| Vector Database | FAISS                             |
| LLM             | Groq Llama 3.1                    |
| NLP             | Semantic Search · RAG             |
| PDF Processing  | PyPDF2                            |
| Deployment      | Streamlit Community Cloud         |

---

# 🧠 System Architecture

```text
PDF Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embedding Generation
   ↓
FAISS Vector Storage
   ↓
Semantic Search
   ↓
Context Retrieval
   ↓
Groq LLM Response
```

---

# ⚡ Quick Start

## Clone Repository

```bash
git clone https://github.com/sarv-tech/Intelligent-Document-Retrieval-System.git
cd Intelligent-Document-Retrieval-System
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 requirements.txt

```txt
streamlit
PyPDF2
langchain
langchain-community
langchain-text-splitters
faiss-cpu
langchain-groq
langchain-huggingface
sentence-transformers
```

---

# 🔑 Setup API Key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Get your API key from:

https://console.groq.com/keys

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📁 Project Structure

```text
/
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── secrets.toml
└── assets/
```

---

# 🌟 Implementation Highlights

### 🔍 Semantic Search

Uses HuggingFace embeddings with FAISS vector storage for intelligent document retrieval.

### ⚡ Fast AI Responses

Integrated Groq’s ultra-fast Llama 3.1 inference engine for low-latency question answering.

### 🧠 Retrieval-Augmented Generation (RAG)

Combines vector retrieval + LLM generation to reduce hallucinations and improve answer relevance.

### 📚 AI Tutor Behavior

Custom prompt engineering enables structured, beginner-friendly educational responses.

---

# 📊 Performance

| Metric             | Value           |
| ------------------ | --------------- |
| PDF Processing     | Real-time       |
| Embedding Speed    | Fast            |
| Query Response     | ~1–3s           |
| Multi-PDF Support  | Yes             |
| Semantic Retrieval | Enabled         |
| Deployment         | Streamlit Cloud |

---

# 🎯 Use Cases

* 📖 AI Study Assistant
* 📄 Smart PDF Reader
* 🧠 Intelligent Note Retrieval
* 🎓 Student Learning Companion
* 🔍 Research Paper Q&A
* 📚 Knowledge Management System

---

# 🔮 Future Roadmap

* 💬 Conversational chat memory
* 🌙 Dark mode UI
* 🔊 Voice assistant integration
* 🖼 OCR for scanned PDFs
* 📌 Source citation highlighting
* 📄 AI-generated summaries
* 🧪 Quiz generation from notes
* 🔐 User authentication system

---

# 👨‍💻 Author

### Sarvesh Pingale
https://www.linkedin.com/in/sarvesh-pingale-8b9090299

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub and sharing it with others.

---

## 🚀 “Turning static notes into intelligent conversations with AI.”
