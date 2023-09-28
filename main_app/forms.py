from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    birthdate = forms.DateField()
    dicord_id = forms.CharField(max_length=100, help_text='Discord ID')
    zoom_id = forms.CharField(max_length=100, help_text='Zoom ID')
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "birthdate", "email", "dicord_id", "zoom_id"]