import { useState } from "react";

import API from "../services/api";

const DocumentAssistant = () => {

  const [file, setFile] = useState(null);

  const [question, setQuestion] = useState("");

  const [answer, setAnswer] = useState("");

  const [loading, setLoading] = useState(false);

  const [uploadMessage, setUploadMessage] =
    useState("");

  const uploadFile = async () => {

    if (!file) return;

    const formData = new FormData();

    formData.append(
      "file",
      file
    );

    try {

      const response = await API.post(
        "/upload-pdf",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data"
          }
        }
      );

      setUploadMessage(
        `Uploaded successfully (${response.data.chunks} chunks created)`
      );

    } catch (error) {

      console.error(error);

      setUploadMessage(
        "Upload failed."
      );
    }
  };

  const askQuestion = async () => {

    if (!question.trim()) return;

    setLoading(true);

    try {

      const response =
        await API.post(
          "/uploaded-chat",
          {
            question
          }
        );

      setAnswer(
        response.data.answer
      );

    } catch (error) {

      console.error(error);

      setAnswer(
        "Error getting answer."
      );
    }

    setLoading(false);
  };

  return (

    <div className="document-assistant">

      <h2>
        Document Intelligence
      </h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) =>
          setFile(
            e.target.files[0]
          )
        }
      />

      <button
        onClick={uploadFile}
      >
        Upload PDF
      </button>

      <p>
        {uploadMessage}
      </p>

      <hr />

      <input
        type="text"
        placeholder="Ask about uploaded report..."
        value={question}
        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }
      />

      <button
        onClick={askQuestion}
      >
        Ask
      </button>

      {loading && (
        <p>
          Thinking...
        </p>
      )}

      {answer && (

        <div
          className="answer-box"
        >

          <h4>
            Answer
          </h4>

          <p>
            {answer}
          </p>

        </div>

      )}

    </div>

  );
};

export default DocumentAssistant;