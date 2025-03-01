import pytest
from django.urls import reverse
from api.models import Todo

@pytest.mark.django_db
def test_create_todo(api_client):
    url = reverse("create") 
    data = {"title": "New Task", "description": "Task Description", "status": 1}
    
    response = api_client.post(url, data, format="json")
    
    assert response.status_code == 201
    assert response.data["title"] == "New Task"

@pytest.mark.django_db
def test_read_todo(api_client, create_todo):
    url = reverse("detail", args=[create_todo.id])  
    
    response = api_client.get(url)
    
    assert response.status_code == 200
    assert response.data["title"] == create_todo.title


