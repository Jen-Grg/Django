from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import *
# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "User registered successfully")
            return redirect('/register')
        else:
            messages.add_message(request, messages.ERROR, "Kindly verify all fields.")
            return render(request, 'user/register.html', {'form': form})
    context = {
        'form': UserCreationForm
    }
    return render(request, 'user/register.html', context)

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data['username'], password = data['password'])
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "You have successfully logged in")
                return redirect('/product/productpage')
            else:
                messages.add_message(request, messages.ERROR, "Kindly verify all the fields")
                return render(request, 'user/login.html', {'form': form})
    return render(request, 'user/login.html', { 'form': LoginForm })
   