from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
           
            form.save()
            
            messages.success(request, f'Your account has been created! You are now able to login ')
            return redirect('login')
    else:
         form = UserRegisterForm()
    return render(request , 'users/register.html', {'form': form})

def login(request):
    return render(request, 'users/login.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')
