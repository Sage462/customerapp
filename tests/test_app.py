<<<<<<< HEAD
from app.app import app

def test_home():
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    assert b"Customer App Running" in response.data


def test_health():
    client = app.test_client()

    response = client.get('/health')

    assert response.status_code == 200
=======
from app.app import app

def test_home():
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    assert b"Customer App Running" in response.data


def test_health():
    client = app.test_client()

    response = client.get('/health')

    assert response.status_code == 200
>>>>>>> 82c0ee0aa98f2cd0823946b1a8e0b3f1dd295783
