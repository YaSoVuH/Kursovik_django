from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, CharField

class RegisterUserForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Никнейм'}))
    password1 = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder':'Пароль'}))
    password2 = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder':'Повторите пароль'}))

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}

    field_order = ['username', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Никнейм'}))
    password = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder':'Пароль'}))

    class Meta:
        model = User
        fields = {'username', 'password'}

    field_order = ['username', 'password']