FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SAMPLE_DATA_DIR=/sample_data

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8005

CMD ["sh", "-c", "python /sample_data/create_database.py && uvicorn app.main:app --host 0.0.0.0 --port 8005 --reload"]
