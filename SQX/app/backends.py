from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# Define a custom authentication backend AdminBackend that only authenticates superusers from the built-in User model.

class AdminBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        CustomUser = get_user_model()
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password) and user.is_superuser:
                return user
        except CustomUser.DoesNotExist:
            return None
        return None