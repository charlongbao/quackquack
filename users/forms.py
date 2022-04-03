from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .widgets import *

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        

class AllSeats(forms.Form):
    date = forms.DateField(widget=DatePickerInput)