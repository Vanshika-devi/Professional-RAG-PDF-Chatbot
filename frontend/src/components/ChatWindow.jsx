import {
  useState,
  useEffect,
  useRef
} from "react";

import { motion } from "framer-motion";

import {
  askQuestion
} from "../api/authApi";

import MessageBubble from "./MessageBubble";

function ChatWindow() {

  const [question, setQuestion] =
    useState("");

  const [messages, setMessages] =
    useState([]);

  const [loading, setLoading] =
    useState(false);

  const messagesEndRef =
    useRef(null);

  useEffect(() => {

    messagesEndRef.current
      ?.scrollIntoView({
        behavior: "smooth"
      });

  }, [messages]);

  const sendQuestion =
    async () => {

      if (
        !question.trim()
      ) return;

      const currentQuestion =
        question;

      setQuestion("");

      setMessages((prev) => [

        ...prev,

        {
          text:
            currentQuestion,

          sender: "user"
        }
      ]);

      try {

        setLoading(true);

        const res =
          await askQuestion(
            currentQuestion
          );

        console.log(
          "AI RESPONSE:",
          res.data
        );

        setMessages((prev) => [

          ...prev,

          {
            text:

              typeof res.data.answer
              === "string"

                ? res.data.answer

                : "Invalid AI response",

            sender: "ai"
          }
        ]);

      } catch (error) {

        console.log(error);

        setMessages((prev) => [

          ...prev,

          {
            text:
              "Failed to get AI response.",

            sender: "ai"
          }
        ]);

      } finally {

        setLoading(false);
      }
    };

  return (

    <motion.div
      className="chat-window"
      initial={{
        opacity: 0,
        y: 20
      }}
      animate={{
        opacity: 1,
        y: 0
      }}
    >

      <div className="chat-top">

        <div>

          <h2>
            AI Assistant
          </h2>

          <p>
            Ask contextual questions
            from uploaded PDFs
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
                Your AI Assistant
                is Ready
              </h3>

              <p>
                Upload a PDF and
                start chatting
                intelligently.
              </p>

            </div>
          )
        }

        {
          messages.map(
            (msg, index) => (

              <MessageBubble
                key={index}
                text={msg.text}
                sender={msg.sender}
              />

            )
          )
        }

        {
          loading && (

            <div className="loading-box">

              AI is thinking...

            </div>
          )
        }

        <div ref={messagesEndRef}></div>

      </div>

      <div className="input-area">

        <input
          type="text"
          placeholder="Ask anything from your PDF..."
          value={question}
          onChange={(e) =>
            setQuestion(
              e.target.value
            )
          }
          onKeyDown={(e) => {

            if (
              e.key === "Enter"
            ) {

              sendQuestion();
            }
          }}
        />

        <button
          onClick={sendQuestion}
          disabled={loading}
        >

          {
            loading
              ? "Thinking..."
              : "Send"
          }

        </button>

      </div>

    </motion.div>
  );
}

export default ChatWindow;