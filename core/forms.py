from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterCoreForm(UserCreationForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']