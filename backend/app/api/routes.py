from fastapi import APIRouter, HTTPException


from app.schemas.query import QueryRequest
from app.schemas.response import QueryResponse

from app.services.query_service import execute_query



router = APIRouter(
    prefix="/api",
    tags=["SQL Analyst"]
)



@router.post(
    "/query",
    response_model=QueryResponse
)
async def query_database(
    request: QueryRequest
):

    try:

        result = execute_query(
            request.question
        )


        return result


    except Exception as e:

        raise HTTPException(

            status_code=400,

            detail=str(e)

        )