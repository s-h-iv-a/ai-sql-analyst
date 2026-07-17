from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database.database import Base


class QueryLog(Base):

    __tablename__ = "query_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    question = Column(
        Text,
        nullable=False
    )

    generated_sql = Column(
        Text,
        nullable=True
    )

    explanation = Column(
        Text,
        nullable=True
    )

    status = Column(
        String(50),
        default="success"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
