from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from Channels.models import Channels


@login_required(login_url='Users:login')
def index(request):
    return render(request, 'Users/index.html', {})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('Users:index')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Users:index')
    return render(request, 'Users/LoginPage.html', {})


@login_required(login_url='Users:login')
def logout_user(request):
    logout(request)
    return redirect('Users:login')


def registration(request):
    if request.user.is_authenticated:
        return redirect('Users:index')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Channels(user=new_user).save()
            return redirect('Users:login')
    else:
        form = RegistrationForm()
    return render(request, 'Users/Registration.html', {'form': form})
