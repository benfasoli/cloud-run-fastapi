from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_example():
    response = client.get('/example')
    assert response.status_code == 200
