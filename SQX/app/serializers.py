from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import exceptions, serializers
from .models import CustomUser

# Serializers define the API representation.

class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already taken. Please choose a different Email.")
        
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user
    
# Customizes JWT default Serializer to add more information about user

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        return token
    
# Custom user call fields

from rest_framework import serializers
from .models import CustomUser 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = '__all__'