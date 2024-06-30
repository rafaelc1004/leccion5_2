from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm, CustomAuthenticationForm, UserEditForm
from django.contrib.auth.decorators import login_required

from seguridad.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request):
    return render(request, 'seguridad/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'seguridad/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'seguridad/login.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('home')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'seguridad/profile.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
