import { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const askSQL = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setResult("");

    try {
      const response = await axios.post(
        "http://localhost:8005/api/query",
        {
          question: question,
        }
      );

      setResult(JSON.stringify(response.data, null, 2));
    } catch (error) {
      setResult(
        "Error connecting to backend: " +
          error.message
      );
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>AI SQL Analyst</h1>

      <p>
        Ask questions about your database using natural language.
      </p>

      <textarea
        placeholder="Example: Show me total sales by month"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={askSQL}>
        {loading ? "Thinking..." : "Ask"}
      </button>

      <div className="result">
        <h2>Result</h2>
        <pre>{result}</pre>
      </div>
    </div>
  );
}

export default App;