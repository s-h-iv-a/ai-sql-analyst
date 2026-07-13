# AI SQL Analyst

Turn natural language questions into SQL, run them against SQLite, and get AI explanations with charts.

## Flow

```
User Question
    ↓
LLM (generate SQL)
    ↓
Validator (read-only check)
    ↓
SQLite (sample sales database)
    ↓
Results
    ↓
AI Explanation
    ↓
Chart (Plotly)
```

## Project Structure

```
ai-sql-analyst/
├── backend/
│   ├── app/
│   │   ├── api/          # REST endpoints
│   │   ├── core/         # Config
│   │   ├── database/     # DB connection
│   │   ├── llm/          # OpenAI SQL + explanation
│   │   ├── services/     # Query orchestration
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Request/response types
│   │   ├── prompts/      # LLM prompt templates
│   │   ├── utils/        # Validator + chart builder
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
├── frontend/             # React UI (coming soon)
├── sample_data/
│   ├── sales.csv
│   ├── customers.csv
│   ├── products.csv
│   └── create_database.py
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Getting Started (Docker)

```bash
docker compose up --build
```

- API: http://localhost:8005
- Docs: http://localhost:8005/docs
- Health: http://localhost:8005/health

## Example Request

```bash
curl -X POST http://localhost:8005/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What were the top selling products?"}'
```

## Environment

Create `backend/.env`:

```
OPENAI_API_KEY=your-key-here
OPENAI_MODEL=gpt-4o-mini
```

## Sample Data

On startup, `sample_data/create_database.py` loads CSVs into `sample_data/sales.db` with three tables:
- `products`
- `customers`
- `sales`
