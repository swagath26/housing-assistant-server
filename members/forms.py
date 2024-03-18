from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'username', 'first_name', 'last_name']