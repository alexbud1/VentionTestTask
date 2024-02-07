import pytest
from rest_framework.test import APIClient
from django.apps import apps


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_registration_valid_input(api_client):
    data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = api_client.post('/api/v1/register/', data)
    assert response.status_code == 200
    assert response.json()['user']['username'] == "testuser"


@pytest.mark.django_db
def test_registration_invalid_input(api_client):
    data = {
        "username": "testuser",
    }
    response = api_client.post('/api/v1/register/', data)
    assert response.status_code == 400
    assert 'password' in response.json()


@pytest.mark.django_db
def test_login_valid_input(api_client):
    # Register a user
    user_data = {"username": "testuser", "password": "testpassword"}
    api_client.post('/api/v1/register/', user_data)

    # Log in
    login_data = {"username": "testuser", "password": "testpassword"}
    response = api_client.post('/api/v1/login/', login_data)
    assert response.status_code == 200
    assert 'access' in response.json()
    assert 'refresh' in response.json()


@pytest.mark.django_db
def test_login_invalid_input(api_client):
    # Register a user
    user_data = {"username": "testuser", "password": "testpassword"}
    api_client.post('/api/v1/register/', user_data)

    # Log in
    login_data = {"username": "testuser", "password": "wrongpassword"}
    response = api_client.post('/api/v1/login/', login_data)
    assert response.status_code == 401
    assert 'No active account found with the given credentials' == response.json()['detail']
