from pyexpat.errors import messages
import re
from django.shortcuts import render, redirect
from .permissions import IsAllowedUser
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from .models import CustomJWTAuthentication, CustomUser
from .forms import ProfileForm, LoginForm
from app import models, validators

# Create your views here.

# Configure home view

def home(request):
    return render(request, 'app/home.html')

# Create a login view

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from rest_framework_simplejwt.tokens import RefreshToken

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = EmailAuthBackend().authenticate(request, email=email, password=password)
            if user is not None and user.is_active:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                })
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'app/login.html'

    def form_valid(self, form):
        refresh = RefreshToken.for_user(self.request.user)

    def get_success_url(self):
        return reverse_lazy('profile')  # redirect to profile view

# Registration form view

from django.contrib.auth.backends import ModelBackend

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except CustomUser.DoesNotExist:
            return None

def register(request):
    authentication_classes = [CustomJWTAuthentication]
    registration_success = False  # Define registration_success variable
    registration_error = 'Please log in'  # Define registration_error variable
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
        if form.is_valid():  # Call is_valid() to trigger validation
            email = form.cleaned_data.get('email')
            if CustomUser.objects.filter(email=email).exists():  # Check if email already exists
                registration_error = 'Email already taken. Please choose a different Email.'
            else:
                custom_user = form.save(commit=False)  # Save the form without committing to the database
                raw_password = form.cleaned_data.get('password1')
                custom_user.set_password(raw_password)  # Set and hash the password
                custom_user.username = email
                custom_user.first_name = form.cleaned_data.get('first_name')  # Save first name
                custom_user.last_name = form.cleaned_data.get('last_name')  # Save last name
                if 'profile_picture' in request.FILES:
                    custom_user.profile_picture = request.FILES['profile_picture']  # Save profile picture
                custom_user.save()  # Save the user to the database
                user = EmailAuthBackend().authenticate(request, email=email, password=raw_password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                    registration_success = True
                    return redirect('home')
                else:
                    # If authentication fails, delete the created user
                    custom_user.delete()
                    registration_error = 'Authentication failed. Please try again.'
    else:
        form = UserRegisterForm()
    return render(request, 'app/register.html', {'form': form, 'registration_success': registration_success, 'registration_error': 'Registration failed'})

# User centre

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser
from django.contrib import messages
from .decorators import jwt_required

@login_required
def profile(request):
    user = request.user
    authentication_classes = [CustomJWTAuthentication]
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)

    if request.GET.get('delete_profile_picture'):
        request.user.profile_picture.delete()
        messages.add_message(request, messages.SUCCESS, 'Profile picture deleted successfully!')
        return redirect('profile')

    if request.GET.get('delete_phone_number'):
        request.user.phone_number = ''
        request.user.save()
        messages.add_message(request, messages.SUCCESS, 'Phone number deleted successfully!')
        return redirect('profile')

    return render(request, 'profile.html', {'form': form})
    
# User list view

from django.contrib.auth.models import User

def user_list_view(request):
    users = User.objects.all()
    return render(request, 'profile.html', {'users': users})

# Replace the serializer with custom variant

from app import serializers
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer

# API views

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .forms import UserRegisterForm
from .serializers import UserRegistrationSerializer
from .models import CustomUser 
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
    
# Register user endpoint

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .forms import UserRegisterForm
from .serializers import UserRegistrationSerializer
from .models import CustomUser 
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserRegisterView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email','first_name','last_name','password1','password2','phone_number'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address'),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
                'password1': openapi.Schema(type=openapi.TYPE_STRING, description='Password1'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password2'),
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
            }
        ),
        responses={
            200: openapi.Response('User created successfully'),
            401: openapi.Response('Invalid credentials')
        }
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if CustomUser.objects.filter(email=request.data.get('email')).exists():
            return Response({'message': 'Email already taken. Please choose a different Email.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Successfully created!',
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        else:
            return Response({'message': 'Invalid request data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
# login user endpoint

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserLoginView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password')
            }
        ),
        responses={
            200: openapi.Response('Userlogged in successfully'),
            401: openapi.Response('Invalid credentials')
        }
    )
    def post(self, request):
        form = LoginForm(request.data)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = EmailAuthBackend().authenticate(request, email=email, password=password)
            if user is not None and user.is_active:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Sucessfully logged in!',
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                })
        else:
            print(form.errors)
            return Response({'message': 'Invalid credentials'}, status=401)

# Error code endpoint

from rest_framework.response import Response
from rest_framework import status

def error_response(error_code, error_message, status_code):
    return Response({'error_code': error_code, 'error_message': error_message}, status=status_code)

# Find users with a certain first name

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser 
from .serializers import UserSerializer

class FindUsersByFirstNameView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('first_name', openapi.IN_PATH, type=openapi.TYPE_STRING, required=True)
        ],
        responses={
            200: openapi.Response('User(s) found successfully'),
            404: openapi.Response('No users found with this first name')
        }
    )
    def get(self, request, *args, **kwargs):
        first_name = kwargs['first_name']
        try:
            users = CustomUser   .objects.filter(first_name=first_name)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser   .DoesNotExist:
            return Response({'message': 'No users found with this first name'}, status=status.HTTP_404_NOT_FOUND)


# Get the profile picture for a user

class GetProfilePicture(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('email', openapi.IN_PATH, type=openapi.TYPE_STRING, required=True)
        ],
        responses={
            200: openapi.Response('Picture found successfully'),
            404: openapi.Response('No user found with this email'),
            401: openapi.Response('No picture found for this user')
        }
    )
    def get(self, request, email, *args, **kwargs):
        try:
            user = CustomUser .objects.get(email=email)  # Fetch the user by email
            if user.profile_picture:  # Check if the user has a profile picture
                return Response({'profile_picture': user.profile_picture.url}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'No picture found for this user'}, status=status.HTTP_401_UNAUTHORIZED)
        except CustomUser .DoesNotExist:
            return Response({'message': 'No user found with this email'}, status=status.HTTP_404_NOT_FOUND)
        
# Edit phone number for the user

class EditPhoneNumber(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('email', openapi.IN_PATH, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('phone_number', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
        ],
        responses={
            200: openapi.Response('Phone number updated successfully'),
            404: openapi.Response('No user found with this email'),
            400: openapi.Response('Invalid phone number format')
        }
    )
    def put(self, request, email, *args, **kwargs):
        try:
            user = CustomUser .objects.get(email=email)  # Fetch the user by email
            phone_number = request.query_params.get('phone_number')  # Get the new phone number from query params
            
            if not phone_number:
                return Response({'message': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Phone number validation for format: +<country_code><number>
            # Example: +1234567890 (where +12 is the country code and 34567890 is the number)

            if not re.match(r'^\+\d{1,3}\d{7,14}$', phone_number):
                return Response({'message': 'Invalid phone number format'}, status=status.HTTP_400_BAD_REQUEST)

            user.phone_number = phone_number  # Update the user's phone number
            user.save()  # Save the changes to the database
            
            return Response({'message': 'Phone number updated successfully', 'phone_number': user.phone_number}, status=status.HTTP_200_OK)
        
        except CustomUser .DoesNotExist:
            return Response({'message': 'No user found with this email'}, status=status.HTTP_404_NOT_FOUND)
        
# Django session log in

class UserSessionLoginView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password')
            }
        ),
        responses={
            200: openapi.Response('User logged in successfully'),
            400: openapi.Response('Invalid form entry'),
            401: openapi.Response('Invalid credentials'),
        }
    )
    def post(self, request):
        form = LoginForm(request.data)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = EmailAuthBackend().authenticate(request, email=email, password=password)
            if user is not None and user.is_active:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return Response({
                    'message': 'Successfully logged in!',
                    'user': {
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'Invalid form data', 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        
# Log out user

from django.contrib.auth import logout

class UserLogoutView(APIView):
    def post(self, request):
        logout(request)  # Log out the user, clearing the session
        return Response({'message': 'Successfully logged out!'}, status=status.HTTP_200_OK)
    
# Current active user in session

from rest_framework.authentication import SessionAuthentication

class CurrentUserView(APIView):
    authentication_classes = [SessionAuthentication]
    def get(self, request):
        if request.user.is_authenticated:
            return Response({'email': request.user.email}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No user is logged in'}, status=status.HTTP_200_OK)