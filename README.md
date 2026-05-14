# RAG PDF Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask contextual questions based on the uploaded content.

Built using React, FastAPI, LangChain, ChromaDB, HuggingFace Embeddings, and Ollama.

---

# Features

* Upload PDF documents
* Ask questions from uploaded PDFs
* Retrieval-Augmented Generation (RAG)
* Semantic search using embeddings
* Vector database integration with ChromaDB
* Local LLM inference using Ollama Phi3
* FastAPI backend APIs
* Modern React frontend UI
* Persistent PDF uploads
* Context-aware AI responses

---

# Tech Stack

## Frontend

* React.js
* CSS3
* Fetch API
* Vite

## Backend

* FastAPI
* Python
* LangChain
* ChromaDB
* Ollama
* PyMuPDF

## AI / ML

* HuggingFace Embeddings
* Sentence Transformers
* RetrievalQA
* Semantic Search

---

# Project Structure

```text
rag-pdf-chatbot/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   │
│   │   ├── services/
│   │   │   ├── embeddings.py
│   │   │   ├── llm_service.py
│   │   │   ├── pdf_loader.py
│   │   │   ├── rag_pipeline.py
│   │   │   └── vector_store.py
│   │   │
│   │   └── main.py
│   │
│   ├── chroma_db/
│   ├── uploads/
│   ├── requirements.txt
│   └── venv/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd rag-pdf-chatbot
```

---

# Backend Setup

## 2. Navigate to Backend

```bash
cd backend
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download Ollama:

[https://ollama.com/download](https://ollama.com/download)

---

# Pull Phi3 Model

```bash
ollama pull phi3
```

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

## 1. Navigate to Frontend

```bash
cd frontend
```

## 2. Install Dependencies

```bash
npm install
```

## 3. Run Frontend

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# How It Works

```text
PDF Upload
     ↓
Text Extraction
     ↓
Chunk Splitting
     ↓
Embeddings Generation
     ↓
ChromaDB Vector Storage
     ↓
Retriever
     ↓
Ollama Phi3
     ↓
AI Response
```

---

# API Endpoints

## Upload PDF

```http
POST /upload
```

Uploads and processes PDF documents.

---

## Ask Questions

```http
POST /ask
```

Request Body:

```json
{
  "question": "What skills are mentioned in the resume?"
}
```

---

# Example Questions

* Summarize this PDF
* What are the key skills?
* Explain the main topic
* What projects are mentioned?
* Who is the author?
* What technologies are used?

---

# AI Pipeline

## PDF Parsing

* PyMuPDF extracts text from uploaded PDFs.

## Chunking

* LangChain RecursiveCharacterTextSplitter splits text into semantic chunks.

## Embeddings

* Sentence Transformers convert text into vector embeddings.

## Vector Database

* ChromaDB stores and retrieves semantic vectors.

## Retrieval

* Relevant chunks are retrieved using similarity search.

## LLM

* Ollama Phi3 generates context-aware responses.

---

# OCR Support

This project also supports OCR (Optical Character Recognition) for scanned and image-based PDFs.

## OCR Features

* Extracts text from scanned PDFs
* Supports image-based documents
* OCR fallback when normal text extraction fails
* Uses Tesseract OCR with PyTesseract

---

# Install OCR Dependencies

```bash
pip install pytesseract pillow pdf2image
```

---

# Install Tesseract OCR

Download and install:

[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

During installation:

* Enable "Add to PATH"
* Install for all users if possible

---

# OCR Workflow

```text
PDF
 ↓
Text Extraction
 ↓
If No Text Found
 ↓
OCR Processing
 ↓
Extracted Text
 ↓
Embeddings
 ↓
Vector Search
 ↓
LLM Response
```

---

# Future Improvements

* JWT Authentication
* Multi-PDF Support
* Chat History
* Streaming Responses
* Source Citations
* Docker Deployment
* OCR Support for Scanned PDFs
* Cloud Deployment
* User Dashboard
* AI Summarization

---

# Performance Notes

Optimized for:

* 8GB RAM systems
* Local AI inference
* Lightweight embedding models

Recommended:

* Close unnecessary applications while running local LLMs.
* Use smaller PDFs for faster embedding generation.

---

# Skills Demonstrated

* Full Stack Development
* AI Integration
* FastAPI Backend Development
* React Frontend Development
* Retrieval-Augmented Generation
* Semantic Search
* Vector Databases
* Local LLM Deployment
* REST API Development
* NLP Pipelines

---

# Resume Description

## Short Version

RAG PDF Chatbot | React.js, FastAPI, LangChain, ChromaDB, Ollama

* Built an AI-powered Retrieval-Augmented Generation chatbot for contextual question answering from uploaded PDF documents.
* Implemented semantic search, embeddings generation, vector database integration, and local LLM inference using Ollama.
* Developed FastAPI backend APIs and responsive React frontend workflows for AI-driven document interaction.

---

# License

This project is for educational and portfolio purposes.
