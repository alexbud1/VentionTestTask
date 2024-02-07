import pytest
from rest_framework.test import APIClient
from django.apps import apps
from django.contrib.auth.models import User
from test_categories import create_category, access_token

Task = apps.get_model('api', 'Task')


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_task(create_category, create_user):
    def _create_task(title, description):
        return Task.objects.create(title=title, description=description, category=create_category("Test category"),
                                   owner=create_user)
    return _create_task


@pytest.fixture
def create_user(api_client):
    user_data = {"username": "testuser1", "password": "testpassword"}
    return User.objects.create_user(username=user_data["username"], password=user_data["password"])


@pytest.mark.django_db
def test_create_task_valid_input(access_token, api_client, create_category, create_user):
    headers = {'Authorization': f'Bearer {access_token}'}
    category_id = create_category("Test category").id
    data = {
        "title": "Test task",
        "description": "Test description",
        "owner": create_user.id,
        "category": category_id
    }
    response = api_client.post('/api/v1/task/', headers=headers, data=data)
    assert response.status_code == 201
    task = Task.objects.first()
    assert task is not None
    assert task.title == "Test task"
    assert task.description == "Test description"
    assert task.category.name == "Test category"
    assert task.owner.username == "testuser1"


@pytest.mark.django_db
def test_create_task_invalid_input(access_token, api_client):
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        "title": "",
        "description": ""
    }
    response = api_client.post('/api/v1/task/', headers=headers, data=data)
    assert response.status_code == 400
    assert response.json() == {
        'description': ['This field may not be blank.'],
        'owner': ['This field is required.'],
        'title': ['This field may not be blank.']}


@pytest.mark.django_db
def test_list_tasks(access_token, api_client, create_task, create_category):
    create_task("Test task 1", "Test description 1")
    create_task("Test task 2", "Test description 2")
    response = api_client.get('/api/v1/task/')
    tasks = response.json()['results']
    assert response.status_code == 200
    assert len(tasks) == 2
    assert tasks[0]['title'] == "Test task 1"
    assert tasks[1]['title'] == "Test task 2"
    assert tasks[0]['description'] == "Test description 1"
    assert tasks[1]['description'] == "Test description 2"
    assert tasks[0]['completed'] is False
    assert tasks[1]['completed'] is False


@pytest.mark.django_db
def test_retrieve_task_valid_case(access_token, api_client, create_task):
    task = create_task("Test task", "Test description")
    response = api_client.get(f'/api/v1/task/{task.id}/')
    assert response.status_code == 200
    task_data = response.json()
    assert task_data["title"] == "Test task"
    assert task_data["description"] == "Test description"
    assert task_data["completed"] is False
    assert task_data["category"] is not None
    assert task_data["owner"] is not None
    assert task_data["category"] == task.category.id


@pytest.mark.django_db
def test_retrieve_task_not_found(access_token, api_client):
    response = api_client.get(f'/api/v1/task/1/')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not found.'}


@pytest.mark.django_db
def test_update_task_valid_input(access_token, api_client, create_task):
    task = create_task("Test task", "Test description")
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        "title": "Updated task",
        "description": "Updated description",
        "completed": True,
        "owner": task.owner.id,
    }
    response = api_client.put(f'/api/v1/task/{task.id}/', headers=headers, data=data)
    assert response.status_code == 200
    task.refresh_from_db()
    assert task.title == "Updated task"
    assert task.description == "Updated description"
    assert task.completed is True


@pytest.mark.django_db
def test_update_task_invalid_input(access_token, api_client, create_task):
    task = create_task("Test task", "Test description")
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        "title": "",
        "description": "",
        "completed": True,
        "owner": task.owner.id,
    }
    response = api_client.put(f'/api/v1/task/{task.id}/', headers=headers, data=data)
    assert response.status_code == 400
    assert response.json() == {
        'title': ['This field may not be blank.'],
        'description': ['This field may not be blank.']
    }


@pytest.mark.django_db
def test_delete_task_valid_case(access_token, api_client, create_task):
    task = create_task("Test task", "Test description")
    headers = {'Authorization': f'Bearer {access_token}'}
    response = api_client.delete(f'/api/v1/task/{task.id}/', headers=headers)
    assert response.status_code == 204
    assert Task.objects.count() == 0


@pytest.mark.django_db
def test_delete_task_not_found(access_token, api_client):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = api_client.delete(f'/api/v1/task/1/', headers=headers)
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found."}
