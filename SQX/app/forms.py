# Form for user registration

from django import forms
from django.core.validators import MinLengthValidator, RegexValidator
from .models import CustomUser
from django.db import models
from django.contrib.auth import login, authenticate
from .validators import validate_image_extension

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number', 'profile_picture')

    first_name = forms.CharField(validators=[MinLengthValidator(2), RegexValidator(r'^[a-zA-Z]+$')])
    last_name = forms.CharField(validators=[MinLengthValidator(2), RegexValidator(r'^[a-zA-Z]+$')])
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(8), RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')])
    password2 = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(8), RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')])
    phone_number = forms.CharField(validators=[RegexValidator(r'^\+\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$')])
    profile_picture = forms.ImageField(validators=[validate_image_extension], required=False)

# Update form

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'profile_picture')

    first_name = forms.CharField(validators=[MinLengthValidator(2), RegexValidator(r'^[a-zA-Z]+$')])
    last_name = forms.CharField(validators=[MinLengthValidator(2), RegexValidator(r'^[a-zA-Z]+$')])
    phone_number = forms.CharField(validators=[RegexValidator(r'^\+\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$')])
    profile_picture = forms.ImageField(validators=[validate_image_extension], required=False)
    new_password = forms.CharField(widget=forms.PasswordInput, label='New Password', required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password', required=False)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and new_password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get('new_password')
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return user

# Log in form

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
            raise forms.ValidationError('Invalid email or password')
        return self.cleaned_data
