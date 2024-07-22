from django.contrib.auth import forms as forms0
from django import forms
from django.contrib.auth.models import User
from .models import *

class SignupForm(forms0.UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
