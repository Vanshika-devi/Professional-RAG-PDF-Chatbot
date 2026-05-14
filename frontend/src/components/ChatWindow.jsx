// frontend/src/components/ChatWindow.jsx

import { useState } from "react";
import { askQuestion } from "../api/ragApi";
import { motion } from "framer-motion";

import MessageBubble from "./MessageBubble";
import Loader from "./Loader";

function ChatWindow() {

  const [question, setQuestion] = useState("");

  const [messages, setMessages] = useState([]);

  const [loading, setLoading] = useState(false);

  const sendQuestion = async () => {

    if (!question) return;

    const userMessage = {
      text: question,
      sender: "user"
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {

      const res = await askQuestion(question);

      const aiMessage = {
        text: res.data.answer,
        sender: "ai"
      };

      setMessages((prev) => [...prev, aiMessage]);

    } catch (error) {

      setMessages((prev) => [
        ...prev,
        {
          text: "Backend not connected yet.",
          sender: "ai"
        }
      ]);
    }

    setLoading(false);

    setQuestion("");
  };

  return (
    <motion.div
      className="chat-window"
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
    >

      <div className="chat-top">

        <div>
          <h2>AI Assistant</h2>

          <p>
            Ask contextual questions from uploaded PDFs
          </p>
        </div>

        <div className="online-status">
          ● Online
        </div>

      </div>

      <div className="messages">

        {
          messages.length === 0 && (

            <div className="empty-chat">

              <div className="empty-icon">
                🤖
              </div>

              <h3>
                Your AI Assistant is Ready
              </h3>

              <p>
                Upload a document and start intelligent conversations with your data.
              </p>

            </div>
          )
        }

        {
          messages.map((msg, index) => (

            <MessageBubble
              key={index}
              text={msg.text}
              sender={msg.sender}
            />

          ))
        }

        {loading && <Loader />}

      </div>

      <div className="input-area">

        <input
          type="text"
          placeholder="Ask anything from your PDF..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendQuestion()}
        />

        <button onClick={sendQuestion}>
          Send
        </button>

      </div>

    </motion.div>
  );
}

export default ChatWindow;