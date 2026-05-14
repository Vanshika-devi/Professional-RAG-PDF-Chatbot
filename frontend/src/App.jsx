// frontend/src/App.jsx

import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const uploadPDF = async () => {
    if (!file) {
      alert("Please select a PDF file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setUploading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          type: "bot",
          text: data.message,
        },
      ]);
    } catch (error) {
      console.log(error);

      setMessages((prev) => [
        ...prev,
        {
          type: "bot",
          text: "PDF upload failed",
        },
      ]);
    }

    setUploading(false);
  };

  const sendQuestion = async () => {
    if (!question.trim()) return;

    const userMessage = {
      type: "user",
      text: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentQuestion = question;

    setQuestion("");

    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/ask",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question: currentQuestion,
          }),
        }
      );

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          type: "bot",
          text: data.answer,
        },
      ]);
    } catch (error) {
      console.log(error);

      setMessages((prev) => [
        ...prev,
        {
          type: "bot",
          text: "Error getting response",
        },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="background-glow glow1"></div>
      <div className="background-glow glow2"></div>

      <header className="navbar">
        <div className="logo-section">
          <div className="logo-box">AI</div>

          <div>
            <h1>RAG PDF Chatbot</h1>
            <p>AI Powered Document Intelligence Platform</p>
          </div>
        </div>

        <div className="nav-buttons">
          <button className="nav-btn dark-btn">
            Dashboard
          </button>

          <button className="nav-btn gradient-btn">
            Upgrade
          </button>
        </div>
      </header>

      <main className="main-container">
        <div className="upload-card">
          <div className="upload-header">
            <h2>Upload Your PDF</h2>

            <p>
              Ask contextual questions from uploaded PDFs
            </p>
          </div>

          <div className="upload-area">
            <input
              type="file"
              accept=".pdf"
              onChange={handleFileChange}
            />

            <button
              onClick={uploadPDF}
              disabled={uploading}
              className="upload-btn"
            >
              {uploading
                ? "Uploading..."
                : "Upload PDF"}
            </button>
          </div>
        </div>

        <div className="chat-container">
          <div className="chat-messages">
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`message ${msg.type}`}
              >
                {msg.text}
              </div>
            ))}

            {loading && (
              <div className="typing">
                Thinking...
              </div>
            )}
          </div>

          <div className="chat-input-section">
            <input
              type="text"
              placeholder="Ask questions from your PDF..."
              value={question}
              onChange={(e) =>
                setQuestion(e.target.value)
              }
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  sendQuestion();
                }
              }}
            />

            <button onClick={sendQuestion}>
              Send
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;