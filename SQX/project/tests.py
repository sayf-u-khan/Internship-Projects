import pytest
from django.test import Client
from django.urls import reverse
from app.views import home, login_view, register, profile

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db
def test_home_view(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200