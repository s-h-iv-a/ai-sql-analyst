import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const askSQL = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await axios.post(
        "http://localhost:8005/api/query",
        {
          question: question,
        }
      );

      setResult(response.data);

    } catch (err) {
      console.error(err);
      setError("Error connecting to backend");
    }

    setLoading(false);
  };


  return (
    <div className="container">

      <header>
        <h1>AI SQL Analyst</h1>
        <p>
          Ask questions about your database using natural language.
        </p>
      </header>


      <section className="query-box">

        <textarea
          placeholder="Example: Show me all customers"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button onClick={askSQL} disabled={loading}>
          {loading ? "Analyzing..." : "Ask"}
        </button>

      </section>


      {error && (
        <div className="error">
          {error}
        </div>
      )}


      {result && (
        <section className="results">


          <div className="card">

            <h2>Generated SQL</h2>

            <pre>
              {result.sql}
            </pre>

          </div>



          <div className="card">

            <h2>Business Explanation</h2>

            <p>
              {result.explanation}
            </p>

          </div>



          <div className="card">

            <h2>Query Results</h2>


            {result.results && result.results.length > 0 ? (

              <table>

                <thead>

                  <tr>

                    {Object.keys(result.results[0]).map((column) => (
                      <th key={column}>
                        {column}
                      </th>
                    ))}

                  </tr>

                </thead>


                <tbody>

                  {result.results.map((row, index) => (

                    <tr key={index}>

                      {Object.values(row).map((value, i) => (

                        <td key={i}>
                          {value}
                        </td>

                      ))}

                    </tr>

                  ))}

                </tbody>


              </table>

            ) : (

              <p>
                No results found.
              </p>

            )}

          </div>


        </section>
      )}

    </div>
  );
}


export default App;