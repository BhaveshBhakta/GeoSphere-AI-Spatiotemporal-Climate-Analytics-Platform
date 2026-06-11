import { useState } from "react";
import API from "../services/api";

const ClimateAssistant = () => {

  const [question, setQuestion] = useState("");

  const [messages, setMessages] = useState([]);

  const [loading, setLoading] = useState(false);

  const askAssistant = async () => {

    if (!question.trim()) return;

    const userMessage = {
      role: "user",
      content: question
    };

    setMessages(prev => [...prev, userMessage]);

    setLoading(true);

    try {

      const response = await API.post(
        "/chat",
        {
          question
        }
      );

      const assistantMessage = {
        role: "assistant",
        content: response.data.answer
      };

      setMessages(prev => [
        ...prev,
        assistantMessage
      ]);

    } catch (error) {

      console.error(error);

      setMessages(prev => [
        ...prev,
        {
          role: "assistant",
          content: "Error generating response."
        }
      ]);

    }

    setQuestion("");

    setLoading(false);
  };

  return (
    <div className="assistant-container">

      <h2>Climate Assistant</h2>

      <div className="chat-window">

        {messages.map((msg, index) => (

          <div
            key={index}
            className={`message ${msg.role}`}
          >
            {msg.content}
          </div>

        ))}

        {loading && (
          <div className="message assistant">
            Thinking...
          </div>
        )}

      </div>

      <div className="chat-input">

        <input
          type="text"
          placeholder="Ask climate questions..."
          value={question}
          onChange={(e) =>
            setQuestion(e.target.value)
          }
        />

        <button onClick={askAssistant}>
          Send
        </button>

      </div>

    </div>
  );
};

export default ClimateAssistant;