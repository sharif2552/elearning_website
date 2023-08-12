# backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from accounts.models import CustomUser


class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password):
            print(user)
            return user
        
        return None
