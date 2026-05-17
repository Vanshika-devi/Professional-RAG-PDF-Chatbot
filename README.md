# 🚀 RAG PDF Chatbot

An AI-powered RAG (Retrieval-Augmented Generation) PDF Chatbot built using FastAPI, React, LangChain, ChromaDB, and Ollama.

This application allows users to upload PDFs and chat with their documents intelligently using local AI models.

---

# ✨ Features

* 🔐 JWT Authentication System
* 📄 Upload and process PDFs
* 🤖 AI-powered contextual question answering
* 🧠 Retrieval-Augmented Generation (RAG)
* 🔎 Semantic search using vector embeddings
* 🗂 ChromaDB vector database
* 🖼 OCR support for scanned PDFs
* 💬 Modern chat interface
* ⚡ FastAPI backend
* 🎨 React frontend with modern UI
* 🧩 LangChain integration
* 🖥 Local LLM support using Ollama + Phi3
* 📚 Works with:

  * Resumes
  * Notes
  * Research papers
  * Assignments
  * Technical documentation
  * OCR PDFs

---

# 🛠 Tech Stack

## Frontend

* React.js
* Vite
* Axios
* Framer Motion
* React Hot Toast

## Backend

* FastAPI
* Python
* JWT Authentication
* LangChain
* ChromaDB
* PyMuPDF
* OCR (Tesseract)

## AI / RAG

* Ollama
* Phi3
* HuggingFace Embeddings
* LangChain RetrievalQA

---

# 🧠 How It Works

## Step 1 — Upload PDF

The uploaded PDF is stored inside:

```bash
backend/uploads/
```

---

## Step 2 — Extract Text

The backend extracts text using:

* PyMuPDF
* OCR fallback using Tesseract for scanned PDFs

---

## Step 3 — Chunking

The document is split into semantic chunks using:

```python
RecursiveCharacterTextSplitter
```

---

## Step 4 — Generate Embeddings

Embeddings are created using:

```python
sentence-transformers/all-MiniLM-L6-v2
```

---

## Step 5 — Store in ChromaDB

Embeddings are stored in:

```bash
backend/chroma_db/
```

---

## Step 6 — Ask Questions

User questions are semantically matched against stored chunks.

The relevant context is sent to the Phi3 model through Ollama.

---

# 📂 Project Structure

```bash
rag-pdf-chatbot/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── auth/
│   │   ├── database/
│   │   ├── models/
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── uploads/
│   ├── chroma_db/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   └── styles/
│   │
│   ├── App.jsx
│   ├── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# ⚙️ Backend Setup

## 1. Navigate to Backend

```bash
cd backend
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Install Ollama

Download Ollama:

[https://ollama.com](https://ollama.com)

---

## 6. Pull Phi3 Model

```bash
ollama pull phi3
```

---

## 7. Create `.env`

Inside `backend/.env`

```env
OLLAMA_MODEL=phi3

MONGO_URL=mongodb://localhost:27017

DATABASE_NAME=rag_pdf_chatbot

SECRET_KEY=mysecretkey123

ALGORITHM=HS256
```

---

## 8. Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# 💻 Frontend Setup

## 1. Navigate to Frontend

```bash
cd frontend
```

---

## 2. Install Dependencies

```bash
npm install
```

---

## 3. Run Frontend

```bash
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# 🔐 Authentication Features

* User Signup
* User Login
* JWT Token Authentication
* Protected API Routes

---

# 🤖 Supported Question Types

## Resume Questions

```txt
What is the candidate name?
What skills are mentioned?
What projects are listed?
What is the CGPA?
```

---

## Notes Questions

```txt
Explain cache coherence.
What is pipelining?
Explain checksum method.
```

---

## Research PDFs

```txt
Summarize the paper.
What methodology is used?
```

---

# 📸 Screenshots

## Login Page

* Modern authentication UI
* JWT-based authentication

## Upload System

* Upload PDF documents
* AI-ready processing

## Chat Interface

* Conversational AI experience
* Real-time answers from PDFs

---

# 🔥 Future Improvements

* Multi-PDF support
* Chat history
* Streaming AI responses
* Source citations
* Dark/Light themes
* Cloud deployment
* User-specific vector databases
* Drag and drop upload
* PDF preview
* Speech-to-text input

---

# 🧪 Example Workflow

1. User logs in
2. Uploads PDF
3. PDF text is extracted
4. Embeddings are generated
5. Chunks stored in ChromaDB
6. User asks questions
7. AI answers using document context

---

# 🚀 API Endpoints

## Auth Routes

### Signup

```http
POST /signup
```

### Login

```http
POST /login
```

---

## PDF Routes

### Upload PDF

```http
POST /upload
```

### Ask Question

```http
POST /ask
```

---

# 🧠 AI Model

This project uses:

```txt
Phi3 via Ollama
```

Optimized for low-end laptops with 8GB RAM.

---

# 👩‍💻 Author

Vanshika Devi

GitHub:

```txt
https://github.com/Vanshika-devi
```

---

# ⭐ If You Like This Project

Give this repository a star ⭐ on GitHub.
