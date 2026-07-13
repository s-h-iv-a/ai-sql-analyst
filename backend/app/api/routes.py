from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.request import QueryRequest
from app.schemas.response import QueryResponse
from app.services.query_service import QueryService

router = APIRouter()
query_service = QueryService()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/query", response_model=QueryResponse)
def ask_question(payload: QueryRequest, db: Session = Depends(get_db)):
    try:
        result = query_service.run(payload.question, db)
        return QueryResponse(**result)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
