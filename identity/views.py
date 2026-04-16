from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from dotenv import load_env
from django.contrib import messages
import os

from .forms import RegisterForm, LoginForm

load_env()

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try: 
                user = form.save()
                send_mail(
                    subject="Account Created Successfully",
                    message=f"Your Username to signin is {user.username}",
                    from_email= os.getenv('EMAIL_HOST_USER'),
                    recipient_list=[user.email],
                    fail_silently=False
                )
                messages.success(request, "Check your email inbox for your account confirmation")
                return redirect('login')
            except Exception as e: 
                messages.error(request, "Error during Creating your account please try again")
                return redirect('register')
    else :
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try: 
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successful")
                    return redirect('profile')
                else:
                    messages.error(request, "Login Fail (Check your Username or Password)")
            except Exception as e :
                messages.error(request, "Login Fail (Check your Username or Password)")
    else :
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                from_email= os.getenv('EMAIL_HOST_USER'),
                subject_template_name='password_reset_subject.txt',
                email_template_name='password_reset_email.html',
            )
            messages.success(request, "Check your email for password reset confirmation")
            return redirect('password_reset_done')
    else :
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user
    context = {
        'username': user.username,
        'email': user.email
    }
    return render(request, 'profile.html', context)