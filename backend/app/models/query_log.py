from sqlalchemy import Column, DateTime, Integer, Text, func

from app.database.database import Base


class QueryLog(Base):
    __tablename__ = "query_logs"

    id = Column(Integer, primary_key=True, index=True)
    natural_language = Column(Text, nullable=False)
    generated_sql = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
