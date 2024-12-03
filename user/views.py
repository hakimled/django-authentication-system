from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    users = User.objects.all()  # Get all users
    context = {'username': request.user.username , 'users':users}
    return render(request, 'user/home.html', context)

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def delete_user(request, user_id):
    # Ensure the user exists
    user = get_object_or_404(User, id=user_id)
    
    # Prevent deleting superuser accounts (optional safeguard)
    if user.is_superuser:
        return redirect('login')  # Redirect to the home page or any error page
    
    # Delete the user
    user.delete()
    
    # Redirect back to the user list
    return redirect('home')

def registation(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')

            form.save()
            form = UserRegisterForm()
            messages.info(request, f'a new user has been registered successfully ')
            
            return  redirect('/')

    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request, 'user/registration.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to your home page
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username or password'})
    return render(request, 'user/login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')
