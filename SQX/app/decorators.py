# JWT access

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from functools import wraps
from rest_framework.response import Response

def jwt_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]

        # Get the user from the request
        user = request.user

        # Check if the user is authenticated
        if not user.is_authenticated:
            return Response({'error': 'Authentication failed'}, status=401)

        # Call the original view function
        return view_func(request, *args, **kwargs)
    return wrapper

