from fastapi.testclient import TestClient
from requests.structures import CaseInsensitiveDict

ADMIN_HEADER = CaseInsensitiveDict(
    data={"Cookie": 'Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hbmFnZXIiLCJuYW1lIjoiRnVsYW5vIGRlIFRhbCIsImpvYl9yb2xlIjoiRXN0YWdpYXJpbyIsImFjY2VzcyI6ImFkbWluIn0.vu3T9_4xAf2UWL8n4c-Wm3pM8JZTAmwdBubrFWgX7nM'})
MANAGER_HEADER = CaseInsensitiveDict(
    data={"Cookie": 'Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hbmFnZXIiLCJuYW1lIjoiRnVsYW5vIGRlIFRhbCIsImpvYl9yb2xlIjoiRXN0YWdpYXJpbyIsImFjY2VzcyI6Im1hbmFnZXIifQ.zftUNuBvt8G19eq0Wqvnd52wBuxzIatQLcSpwIrWkUQ'})
BASIC_HEADER = CaseInsensitiveDict(
    data={"Cookie": 'Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hbmFnZXIiLCJuYW1lIjoiRnVsYW5vIGRlIFRhbCIsImpvYl9yb2xlIjoiRXN0YWdpYXJpbyIsImFjY2VzcyI6ImJhc2ljIn0.YOEKPNoyA5xK0X4R1z3KNB-v9E2Oy1AokmzArx-2bks'})


def test_delete_user_as_admin(client: TestClient):
    response = client.delete("/user/user_K", headers=ADMIN_HEADER)
    assert response.status_code == 200
    assert response.json()["message"] == "Dados deletados com sucesso"


def test_delete_user_as_manager(client: TestClient):
    response = client.delete("/user/user_A", headers=MANAGER_HEADER)
    assert response.status_code == 401
    assert response.json()["message"] == "Acesso negado"


def test_delete_user_as_basic(client: TestClient):
    response = client.delete("/user/user_A", headers=BASIC_HEADER)
    assert response.status_code == 401
    assert response.json()["message"] == "Acesso negado"
