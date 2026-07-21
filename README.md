# 🤖 AI SQL Analyst

> An AI-powered natural language SQL analyst that lets users ask questions about their database in plain English and receive generated SQL, business-friendly explanations, and query results.

## 🌐 Live Demo

**Try the application:**
[https://sql-bot-mu.vercel.app/](https://sql-bot-mu.vercel.app/?utm_source=chatgpt.com)

---

## 📌 Overview

AI SQL Analyst is a full-stack application that allows users to interact with structured database data using natural language.

Instead of manually writing SQL queries, users can simply ask questions such as:

> "Show me all tables"

> "What are the top-selling products?"

> "Show me total sales by month"

The application uses an LLM-powered backend to understand the user's question, generate an appropriate SQL query, execute it against the database, and return the results along with a clear business-oriented explanation.

The goal is to make data analysis more accessible to users who may not have extensive SQL knowledge.

---

## ✨ Features

* 💬 **Natural Language to SQL**

  * Ask database questions using plain English.
  * Automatically generate SQL queries using an LLM.

* 🧠 **AI-Powered Query Analysis**

  * Converts user questions into executable SQL.
  * Provides explanations of generated queries.

* 📊 **Business-Friendly Insights**

  * Explains query results in simple, analyst-friendly language.
  * Highlights important numbers and business interpretations.

* 📋 **Dynamic Query Results**

  * Displays returned database records in a structured table.

* 💻 **Interactive Web Interface**

  * Clean React-based user interface.
  * Supports multiple questions and conversation history.

* 🔌 **REST API**

  * FastAPI backend exposes a query endpoint for database analysis.

* 🗄️ **SQLite Database**

  * Includes sample data for customers, products, sales, and query logs.

* 🐳 **Dockerized Architecture**

  * Frontend and backend run in separate Docker containers.
  * Easy local development and deployment.

* ☁️ **Cloud Deployment**

  * Frontend deployed with Vercel.
  * Backend deployed with Render.

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │       User           │
                         │  Natural Language    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   React Frontend     │
                         │   Vite + Axios       │
                         │      Vercel          │
                         └──────────┬───────────┘
                                    │
                              HTTP REST API
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   FastAPI Backend    │
                         │      Render          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   AI / LLM Layer     │
                         │  Natural Language →  │
                         │        SQL           │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    SQLite Database   │
                         │                      │
                         │  customers            │
                         │  products             │
                         │  sales                │
                         │  query_logs           │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Query Results +      │
                         │ Business Explanation │
                         └──────────────────────┘
```

---

## 🔄 How It Works

1. The user enters a question in natural language.
2. The React frontend sends the question to the FastAPI backend.
3. The backend provides the database schema and context to the LLM.
4. The LLM generates a SQL query based on the user's question.
5. The backend validates and executes the generated SQL query.
6. The database returns the requested records.
7. The application generates a business-friendly explanation.
8. The frontend displays:

   * Generated SQL
   * Business explanation
   * Query results

### Example

**User Question**

```text
Show me all tables
```

**Generated SQL**

```sql
SELECT name
FROM sqlite_master
WHERE type = 'table';
```

**Result**

```text
customers
products
sales
query_logs
```

**Business Interpretation**

The database contains four primary data entities that can be used for customer analysis, product analysis, sales reporting, and query activity monitoring.

---

## 🛠️ Tech Stack

### Frontend

* React
* Vite
* Axios
* JavaScript
* CSS

### Backend

* Python
* FastAPI
* Uvicorn
* SQLAlchemy
* Pydantic

### AI / LLM

* LLM-powered natural language to SQL generation
* AI-generated SQL explanations
* Business-oriented result interpretation

### Database

* SQLite
* SQLAlchemy ORM
* Sample customer, product, sales, and query log data

### DevOps & Deployment

* Docker
* Docker Compose
* Git
* GitHub
* Vercel
* Render

---

## 📁 Project Structure

```text
ai-sql-analyst/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │
│   │   ├── core/
│   │   │   └── config.py
│   │   │
│   │   ├── database/
│   │   │   └── connection.py
│   │   │
│   │   ├── llm/
│   │   │   ├── sql_generator.py
│   │   │   └── explainer.py
│   │   │
│   │   ├── models/
│   │   │
│   │   ├── prompts/
│   │   │
│   │   ├── schemas/
│   │   │
│   │   ├── services/
│   │   │   └── query_service.py
│   │   │
│   │   ├── utils/
│   │   │   ├── validator.py
│   │   │   └── chart_builder.py
│   │   │
│   │   └── main.py
│   │
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── sample.db
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.js
│
├── sample_data/
│   ├── sales.csv
│   ├── customers.csv
│   ├── products.csv
│   └── create_database.py
│
├── docker-compose.yml
├── main.py
└── README.md
```

---

## 🚀 Running Locally

### Prerequisites

Make sure you have:

* Docker
* Docker Compose
* Git

You do not need to install Node.js or npm on the host machine when using the Docker setup.

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ai-sql-analyst
```

### 2. Configure environment variables

Create:

```text
backend/.env
```

Add your required LLM API configuration.

For example:

```env
OPENAI_API_KEY=your_api_key_here
```

> Never commit API keys or secrets to GitHub.

### 3. Start the application

```bash
docker compose up --build
```

### 4. Open the frontend

```text
http://localhost:5173
```

### 5. Open the backend API documentation

```text
http://localhost:8005/docs
```

---

## 🔌 API

### Query Database

```http
POST /api/query
```

### Request

```json
{
  "question": "Show me all tables"
}
```

### Response

```json
{
  "sql": "SELECT name FROM sqlite_master WHERE type='table'",
  "explanation": "Business-friendly explanation of the query and results.",
  "results": [
    {
      "name": "customers"
    },
    {
      "name": "products"
    },
    {
      "name": "sales"
    },
    {
      "name": "query_logs"
    }
  ],
  "chart": {}
}
```

---

## 🔐 Security Considerations

The application includes a SQL validation layer to help control AI-generated database queries before execution.

For production environments, additional security measures should be considered, including:

* Read-only database credentials
* Strict SQL allowlisting
* Query timeouts
* Rate limiting
* Authentication and authorization
* Input validation
* Protection against prompt injection
* Database access isolation
* Secret management
* Production-grade persistent database storage

---

## ☁️ Deployment

The application is deployed using a split frontend/backend architecture.

### Frontend

**Platform:** Vercel

**Live Application:**
[https://sql-bot-mu.vercel.app/](https://sql-bot-mu.vercel.app/?utm_source=chatgpt.com)

### Backend

**Platform:** Render

The frontend communicates with the FastAPI backend through the deployed REST API.

```text
Vercel
React + Vite
    │
    │ HTTPS API Request
    ▼
Render
FastAPI
    │
    ▼
LLM + SQL Database
```

---

## 🎯 Project Goals

This project was built to explore the intersection of:

* Generative AI
* Natural Language Processing
* SQL
* Data Analytics
* Backend API Development
* Full-Stack Engineering
* Containerization
* Cloud Deployment

The project demonstrates how an AI-powered application can bridge the gap between natural language and structured data analysis.

---

## 🔮 Future Improvements

Planned improvements include:

* [ ] Interactive charts and visualizations
* [ ] Database schema explorer
* [ ] CSV export
* [ ] Query result downloads
* [ ] Persistent conversation history
* [ ] User authentication
* [ ] Multi-database support
* [ ] PostgreSQL production database
* [ ] Query caching
* [ ] Streaming AI responses
* [ ] Advanced SQL safety and validation
* [ ] Role-based database access
* [ ] Improved prompt injection protection

---

## 👨‍💻 Author

**Shiva Saidula**

Built as a full-stack AI application demonstrating natural language database interaction, LLM-powered SQL generation, data analysis, and cloud deployment.

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub!
