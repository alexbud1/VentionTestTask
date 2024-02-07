import pytest
from rest_framework.test import APIClient
from django.apps import apps

Category = apps.get_model('api', 'Category')


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_category():
    def _create_category(name):
        return Category.objects.create(name=name)
    return _create_category


@pytest.fixture
def access_token(api_client):
    # Register a user
    user_data = {"username": "testuser", "password": "testpassword"}
    api_client.post('/api/v1/register/', user_data)

    # Log in
    login_data = {"username": "testuser", "password": "testpassword"}
    response = api_client.post('/api/v1/login/', login_data)

    return response.json()['access']


@pytest.mark.django_db
def test_create_category_valid_input(access_token, api_client):
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        "name": "Test category"
    }
    response = api_client.post('/api/v1/category/', headers=headers, data=data)
    assert response.status_code == 201
    category = Category.objects.first()
    assert category is not None
    assert category.name == "Test category"


@pytest.mark.django_db
def test_create_category_invalid_input(access_token, api_client):
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        "name": ""
    }
    response = api_client.post('/api/v1/category/', headers=headers, data=data)
    assert response.status_code == 400
    assert response.json() == {'name': ['This field may not be blank.']}


@pytest.mark.django_db
def test_list_categories(access_token, api_client, create_category):
    create_category("Test category 1")
    create_category("Test category 2")
    response = api_client.get('/api/v1/category/')

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["count"] == 2
    assert response_data["next"] is None
    assert response_data["previous"] is None
    category_names = [category["name"] for category in response_data["results"]]
    assert "Test category 1" in category_names
    assert "Test category 2" in category_names


@pytest.mark.django_db
def test_retrieve_category_valid_case(access_token, api_client, create_category):
    category = create_category("Test category")
    response = api_client.get(f'/api/v1/category/{category.id}/')

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == category.id
    assert response_data["name"] == "Test category"


@pytest.mark.django_db
def test_retrieve_category_not_found(access_token, api_client):
    response = api_client.get(f'/api/v1/category/1/')
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found."}


@pytest.mark.django_db
def test_update_category_valid_input(access_token, api_client, create_category):
    category = create_category("Test category")
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        "name": "Updated category"
    }
    response = api_client.put(f'/api/v1/category/{category.id}/', headers=headers, data=data)
    assert response.status_code == 200
    category.refresh_from_db()
    assert category.name == "Updated category"


@pytest.mark.django_db
def test_update_category_invalid_input(access_token, api_client, create_category):
    category = create_category("Test category")
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        "name": ""
    }
    response = api_client.put(f'/api/v1/category/{category.id}/', headers=headers, data=data)
    assert response.status_code == 400
    assert response.json() == {'name': ['This field may not be blank.']}


@pytest.mark.django_db
def test_delete_category_valid_case(access_token, api_client, create_category):
    category = create_category("Test category")
    headers = {'Authorization': f'Bearer {access_token}'}
    response = api_client.delete(f'/api/v1/category/{category.id}/', headers=headers)
    assert response.status_code == 204
    assert Category.objects.count() == 0


@pytest.mark.django_db
def test_delete_category_not_found(access_token, api_client):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = api_client.delete(f'/api/v1/category/1/', headers=headers)
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found."}
