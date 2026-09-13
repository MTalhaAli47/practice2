from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_positive():
    response = client.get("/predict?x=5")
    assert response.status_code == 200
    assert response.json() == {"prediction": 10}


def test_predict_zero():
    response = client.get("/predict?x=0")
    assert response.status_code == 200
    assert response.json() == {"prediction": 0}


def test_predict_negative():
    response = client.get("/predict?x=-5")
    assert response.status_code == 200
    assert response.json() == {"prediction": -10}
