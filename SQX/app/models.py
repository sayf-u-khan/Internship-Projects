from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group, PermissionsMixin, Permission, BaseUserManager
from django.core import validators
from django.utils.translation import gettext_lazy as _

# User profile using django user

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    
# Normal custom user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(auto_created=True, primary_key=True)
    first_name = models.CharField(max_length=25, validators=[
        validators.MinLengthValidator(2),
        validators.RegexValidator(r'^[a-zA-Z]+$')
    ])
    last_name = models.CharField(max_length=25, validators=[
        validators.MinLengthValidator(2),
        validators.RegexValidator(r'^[a-zA-Z]+$')
    ])
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, validators=[
        validators.RegexValidator(r'^\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$')
    ])
    profile_picture = models.ImageField(upload_to='profile_pictures/')

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        related_name='custom_user_set',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.')
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        related_name='custom_user_set',
        blank=True,
        help_text=_('Specific permissions for this user.')
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    def __str__(self):
        return self.email
    
# Define a custom JWT auth class

from rest_framework_simplejwt.authentication import JWTAuthentication
from app.models import CustomUser

class CustomJWTAuthentication(JWTAuthentication):
    user_model = CustomUser
    
    