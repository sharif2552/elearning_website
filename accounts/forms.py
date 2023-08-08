# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPES)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'password1', 'password2', 'user_type')
