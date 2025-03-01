import pytest
from rest_framework.test import APIClient
from api.models import Todo, User


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    return User.objects.create_user(email="testuser@example.com", name="Test User", password="testpassword")

@pytest.fixture
def create_todo(db, create_user):
    return Todo.objects.create(
        user=create_user,
        title="Test Task",
        description="This is a test task",
        status="1"
    )
