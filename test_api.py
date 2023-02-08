from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_get_current_datetimes():
    response = client.get("/current-datetimes?city1=Chicago,IL&city2=New York,NY")
    assert response.status_code == 200


def test_get_current_datetimes_temp():
    response = client.get("/current-datetimes-temp?city1=Chicago,IL&city2=New York,NY")
    assert response.status_code == 200