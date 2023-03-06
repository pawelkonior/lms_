from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import forms


def registration_view(request):
    form = forms.RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect(reverse_lazy('home:home'))
    return render(request, 'users/registration.html', {'form': form})
