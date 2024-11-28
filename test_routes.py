import pytest
from myapp import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_read_product(client):
    response = client.get("/products/1")
    assert response.status_code == 200

def test_update_product(client):
    response = client.put("/products/1", json={"name": "Smartphone"})
    assert response.status_code == 200

def test_delete_product(client):
    response = client.delete("/products/1")
    assert response.status_code == 204

def test_list_all_products(client):
    response = client.get("/products")
    assert response.status_code == 200

def test_list_by_name(client):
    response = client.get("/products?name=Laptop")
    assert response.status_code == 200

def test_list_by_category(client):
    response = client.get("/products?category=Electronics")
    assert response.status_code == 200

def test_list_by_availability(client):
    response = client.get("/products?availability=True")
    assert response.status_code == 200
