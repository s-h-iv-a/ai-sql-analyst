from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_root():

    response = client.get("/")

    assert response.status_code == 200



def test_query_endpoint():

    response = client.post(

        "/api/query",

        json={
            "question":
            "Show all customers"
        }

    )


    assert response.status_code in [
        200,
        400
    ]
