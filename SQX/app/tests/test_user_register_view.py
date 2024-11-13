from django.test import Client, TestCase

# Create your tests here.

import pytest
from django.urls import reverse
from rest_framework import status
from app.models import CustomUser
from app.views import UserRegisterView

@pytest.mark.django_db  # This is required to allow database access in tests
class TestUserRegisterView:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = reverse('UserRegisterView')  # Replace with the actual URL name for your UserRegisterView
        self.valid_payload = {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!',
            'phone_number': '+441234567890'
        }

    def test_register_user_success(self, client: Client):
        response = client.post(self.url, self.valid_payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Successfully created!'
        assert CustomUser .objects.filter(email='testuser@example.com').exists()

    def test_register_user_email_already_exists(self, client: Client):
        # First create the user
        client.post(self.url, self.valid_payload, format='json')
        
        # Attempt to register again with the same email
        response = client.post(self.url, self.valid_payload, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'Email already taken. Please choose a different Email.' in response.data['message']

    def test_register_user_invalid_data(self, client: Client):
        invalid_payload = {
            'email': 'invalidemail',  # Invalid email format
            'first_name': '',
            'last_name': 'User ',
            'password1': 'TestPassword123!',
            'password2': 'differentpassword',  # Passwords do not match
            'phone_number': '1234567890'
        }
        response = client.post(self.url, invalid_payload, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'Invalid request data' in response.data['message']
        assert 'errors' in response.data
