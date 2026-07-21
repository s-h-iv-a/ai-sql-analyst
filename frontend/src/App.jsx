import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const askSQL = async () => {
    if (!question.trim()) return;

    const currentQuestion = question;

    setQuestion("");
    setLoading(true);
    setError("");

    try {
      const response = await axios.post(
        `${import.meta.env.VITE_API_URL}/api/query`,
        {
          question: currentQuestion,
        }
      );

      setChat((prev) => [
        ...prev,
        {
          question: currentQuestion,
          answer: response.data,
        },
      ]);

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
          placeholder="Example: Show me total sales by product"
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



      {chat.map((item, index) => (

        <section className="results" key={index}>


          <div className="card question-card">

            <h2>
              Question
            </h2>

            <p>
              {item.question}
            </p>

          </div>



          <div className="card">

            <h2>
              Generated SQL
            </h2>

            <pre>
              {item.answer.sql}
            </pre>

          </div>



          <div className="card">

            <h2>
              Business Explanation
            </h2>

            <p>
              {item.answer.explanation}
            </p>

          </div>



          <div className="card">

            <h2>
              Query Results
            </h2>


            {item.answer.results?.length > 0 ? (

              <table>

                <thead>

                  <tr>

                    {Object.keys(
                      item.answer.results[0]
                    ).map((column) => (

                      <th key={column}>
                        {column}
                      </th>

                    ))}

                  </tr>

                </thead>


                <tbody>

                  {item.answer.results.map(
                    (row, rowIndex) => (

                    <tr key={rowIndex}>

                      {Object.values(row).map(
                        (value, i) => (

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

      ))}


    </div>
  );
}

export default App;