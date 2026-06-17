import { useState } from "react";
import API from "../services/api";

const ClimateAssistant = ({
  city
}) => {

  const [question, setQuestion] = useState("");

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hello! I am your Climate Intelligence Assistant. Ask me about weather, climate change, predictions, AQI, or climate reports."
    }
  ]);

  const [loading, setLoading] = useState(false);

  const askAssistant = async () => {

    if (!question.trim()) return;

    const currentQuestion = question;

    setMessages(prev => [
      ...prev,
      {
        role: "user",
        content: currentQuestion
      }
    ]);

    setQuestion("");

    setLoading(true);

    try {

      const response = await API.post(
        "/agent-chat",
        {
          question: currentQuestion,
          city: city
        }
      );

      setMessages(prev => [
      ...prev,
      {
        role: "assistant",

        content:
          response.data.answer ||
          "No response generated.",

        route:
          response.data.route || null
      }
    ]);

    } catch (error) {

      console.error(error);

      setMessages(prev => [
        ...prev,
        {
          role: "assistant",
          content:
            "Unable to contact Climate Agent."
        }
      ]);

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="assistant-container">

      <h2>
        Climate Intelligence Agent
      </h2>

      <div className="chat-window">

        {messages.map((msg, index) => (

          <div
            key={index}
            className={`message ${msg.role}`}
          >

            {msg.route && (

              <div
                className="route-badge"
              >
                {msg.route.toUpperCase()}
              </div>

            )}

            {msg.content}

          </div>

        ))}

        {loading && (

          <div className="message assistant">
            Analyzing...
          </div>

        )}

      </div>

      <div className="chat-input">

        <input
          type="text"
          placeholder="Ask anything about climate..."
          value={question}
          onChange={(e) =>
            setQuestion(e.target.value)
          }
          onKeyDown={(e) => {

            if (e.key === "Enter") {

              askAssistant();

            }

          }}
        />

        <button
          onClick={askAssistant}
        >
          Send
        </button>

      </div>

    </div>
  );
};

export default ClimateAssistant;