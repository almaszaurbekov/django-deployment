from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from core.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    return render(request, "core/main.html", {})

def error(request):
    return render(request, "core/error.html", {})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main')
    else:
        form = UserLoginForm()
    return render(request, 'core/login.html', {'form': form})

def user_update(request):
    user = request.user
    if request.method == 'POST':
        print(request.POST)
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'core/user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')
