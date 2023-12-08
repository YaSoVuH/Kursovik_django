from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from . import forms

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def login(request):
    return render(request, 'main/about.html')

class RegisterUser(CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'main/register.html'
    success_url = '/'

class LoginUser(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'main/login.html'
    success_url = '/'

def logout_user(request):
    logout(request)
    return redirect('login')