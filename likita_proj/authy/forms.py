from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from base.models import User
from django import forms

class MyUserCreationForm(UserCreationForm):
    
    
    class Meta:
        model = User
        fields = ['name', 'username','email', 'location', 'password1', 'password2']
        