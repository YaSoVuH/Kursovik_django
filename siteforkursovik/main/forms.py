from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, CharField

class RegisterUserForm(UserCreationForm):
    username = CharField(label="Логин*: ")
    password1 = CharField(label="Пароль*: ")
    password2 = CharField(label="Повторить пароль*: ")

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}
        widgets = {
            'username': TextInput(attrs={'class': 'form-input'}),
            'password1': PasswordInput(attrs={'class': 'form-input'}),
            'password2': PasswordInput(attrs={'class': 'form-input'}),
        }

    field_order = ['username', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = CharField(label="Логин*: ")
    password = CharField(label="Пароль*: ")

    class Meta:
        model = User
        fields = {'username', 'password'}
        widgets = {
            'username': TextInput(attrs={'class': 'form-input'}),
            'password': PasswordInput(attrs={'class': 'form-input'}),
        }

    field_order = ['username', 'password']