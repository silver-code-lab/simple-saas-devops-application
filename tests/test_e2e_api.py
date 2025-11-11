import requests, time, os
BASE = os.getenv("BASE_URL", "http://localhost:8000")

def wait_ready():
    for _ in range(30):
        try:
            r = requests.get(f"{BASE}/health", timeout=2)
            if r.ok: return True
        except Exception:
            pass
        time.sleep(1)
    return False

def test_end_to_end():
    assert wait_ready()
    payload = {"id":"123","name":"Ada","email":"ada@example.com"}
    r = requests.post(f"{BASE}/person/123", json=payload, timeout=5)
    assert r.status_code == 200
    r = requests.get(f"{BASE}/person", timeout=5)
    assert r.status_code == 200
    assert any(p.get("email")=="ada@example.com" for p in r.json())
