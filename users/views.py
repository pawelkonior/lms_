from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import forms


def registration_view(request):
    form = forms.RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect(reverse_lazy('users:login'))
    return render(request, 'users/registration.html', {'form': form})


def login_user_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse_lazy('home:home'))
    else:
        form = forms.LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('home:home'))
