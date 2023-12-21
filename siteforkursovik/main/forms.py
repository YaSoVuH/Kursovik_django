from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, CharField

class RegisterUserForm(UserCreationForm):


    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}
        widgets = {
            'username': TextInput(attrs={'class': 'form-input'}),
            'password1': PasswordInput(attrs={'class': 'form-input', 'type': 'password'}),
            'password2': PasswordInput(attrs={'class': 'form-input', 'type': 'password'}),
        }

    field_order = ['username', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):

    class Meta:
        model = User
        fields = {'username', 'password'}
        widgets = {
            'username': TextInput(attrs={'class': 'form-input'}),
            'password': PasswordInput(attrs={'class': 'form-input', 'type': 'password'}),
        }

    field_order = ['username', 'password']