from fastapi.testclient import TestClient

from platform_bootstrap_api.main import app


client = TestClient(app)


def test_healthz_ok() -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_bootstrap_ok() -> None:
    payload = {"owner": "octo-org", "repo": "demo-repo"}
    response = client.post("/bootstrap", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["ok"] is True
    assert isinstance(body["actions"], list)
    assert body["dry_run"] is True
