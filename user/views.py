from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout


# Create your views here.

def signup(request):
    if request.method=="GET":
        signupForm=UserCreationForm()
        return render(request, 'user/signup_basic.html', {'signupForm':signupForm})
    elif request.method=="POST":
        signupForm=UserCreationForm(request.POST)
        if signupForm.is_valid():
            user=signupForm.save(commit=False)
            user.save()
            return redirect('/')

def login(request):
    if request.method=="GET":
        loginForm=AuthenticationForm()
        return render(request, 'user/login_basic.html', {'loginForm': loginForm})
    elif request.method=="POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
            return redirect('/')
        else:
            loginForm=AuthenticationForm()
            return render(request, 'user/login_basic.html', {'loginForm': loginForm})

def logout(request):
    auth_logout(request)
    return redirect('/')

