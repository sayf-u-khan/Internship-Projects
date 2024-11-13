import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.urls import reverse

@pytest.mark.django_db
class TestUserLoginView:
    def setup_method(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='TestPassword123!'
        )
        self.url = reverse('UserLoginView')

    def test_login_success(self):
        data = {'email': 'test@example.com', 'password': 'TestPassword123!'}
        response = self.client.post(self.url, data, format='json')
        assert response.status_code == 200
        assert 'message' in response.data
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_login_failure_invalid_credentials(self):
        data = {'email': 'test@example.com', 'password': 'wrongpassword'}
        response = self.client.post(self.url, data, format='json')
        assert response.status_code == 401
        assert 'message' in response.data

    def test_login_failure_missing_email(self):
        data = {'password': 'password123'}
        response = self.client.post(self.url, data, format='json')
        assert response.status_code == 401
        assert 'message' in response.data

    def test_login_failure_missing_password(self):
        data = {'email': 'test@example.com'}
        response = self.client.post(self.url, data, format='json')
        assert response.status_code == 401
        assert 'message' in response.data

    def test_login_failure_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        data = {'email': 'test@example.com', 'password': 'password123'}
        response = self.client.post(self.url, data, format='json')
        assert response.status_code == 401
        assert 'message' in response.data